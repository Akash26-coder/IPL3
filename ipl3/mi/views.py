from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Rohit</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Hardik</h1>')