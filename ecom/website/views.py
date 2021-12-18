from django.shortcuts import render
from django.http.response import JsonResponse
# from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Product, Customer, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password


def index(request):
    products = Product.objects.all()
    data = {
        "products": products
    }
    return render(request, 'index.html', context=data)


def Register(request):
    if(request.user.is_authenticated):
        # messages.success(request, 'Logged in already ')
        return redirect('index')
    
    print("request.POST = ", request.POST)
    if request.POST.get('username') and request.POST.get('password'):
        user = User.objects.create(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        c = Customer.objects.create(
            user=user,
            name=request.POST.get('username'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            email=request.POST.get('username')
        )
        print("creted user = ", c)
        # messages.success(request, 'Created account for User.  ')
        login(request, user)
        return redirect('index')
    else:
        print("error at register.")
    return render(request, 'register.html', context={})


def Login(request):
    if(request.user.is_authenticated):
        # messages.success(request, 'Logged in already ')
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            # user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
        except:
            user = None
        if user and (check_password(password, user.password) and user.is_active):
            login(request, user)
            return redirect('index')
        else:
            print("not is_authenticated.")
    else:
        print("not request.method == 'POST'.")
    return render(request, 'login.html', context={})


def Logout(request):
    logout(request)
    return render(request, 'login.html', context={})


def about(request):
    # return HttpResponse("About Us page.")
    return render(request, 'about.html', context={})


def contact(request):
    # return HttpResponse("Contact Us page.")
    return render(request, 'contact.html', context={})


def services(request):
    # return HttpResponse("services Us page.")
    return render(request, 'services.html', context={})


def json_resp(request):
    return JsonResponse({"success": True, "message_info": "API Response in JSON."})
