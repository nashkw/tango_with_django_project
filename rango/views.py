from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>Go to about page</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/'>Back to index page</a>")