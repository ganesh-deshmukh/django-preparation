from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


def index(request):
    # return HttpResponse("Index page.")
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Us page.")


def json_resp(request):
    return JsonResponse({"success": True, "message_info": "API Response in JSON."})
