# from django.shortcuts import render, HttpResponse, JsonResponse
from django.http.response import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Index page.")


def about(request):
    return HttpResponse("About Us page.")


def json(request):
    return JsonResponse({"success": True})
