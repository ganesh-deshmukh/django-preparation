from django.shortcuts import render
from django.http.response import JsonResponse
# from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout


def index(request):
    products = Product.objects.all()
    data = {
        "products": products
    }
    return render(request, 'index.html', context=data)


def login(request):
    return render(request, 'login.html', context={})


def register(request):

    return render(request, 'register.html', context={})


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
