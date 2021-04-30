from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def heart_pred(request):
    return render(request, 'about.html')

def liver_pred(request):
    return render(request, 'about.html')

def stroke_pred(request):
    return render(request, 'about.html')
