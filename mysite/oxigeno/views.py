from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the oxigeno index.")

def rest_get(request):
    return HttpResponse("Hello, world. You're at the oxigeno get api.")
