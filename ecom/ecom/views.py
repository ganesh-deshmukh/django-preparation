from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


def index(request):
    data = {
        "product": "Iphone",
        "price": "1000$"
    }
    return render(request, 'index.html', context=data)
    # return HttpResponse("Index page.")


def about(request):
    return HttpResponse("About Us page.")


def json_resp(request):
    return JsonResponse({"success": True, "message_info": "API Response in JSON."})
