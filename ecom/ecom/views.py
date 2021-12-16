from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Index page.")


def about(request):
    return HttpResponse("About Us page.")
