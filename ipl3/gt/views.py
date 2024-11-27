from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain1(request):
    return HttpResponse('<h1>Gill</h1>')

def vicecaptain1(request):
    return HttpResponse('<h1>shami</h1>')