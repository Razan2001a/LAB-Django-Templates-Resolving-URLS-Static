from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/home.html')

def terms_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/terms.html')