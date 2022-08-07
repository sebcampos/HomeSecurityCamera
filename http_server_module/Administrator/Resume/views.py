from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', context={})

def automation(request):
    return render(request, 'automation_page.html', context={})

def data_science(request):
    return render(request, 'data_science.html', context={})

def web_development(request):
    return render(request, 'web_development.html', context={})

def backend(request):
    return render(request, 'backend.html', context={})

def app_development(request):
    return render(request, 'app_development.html', context={})

def machine_learning(request):
    return render(request, 'machine_learning.html', context={})

