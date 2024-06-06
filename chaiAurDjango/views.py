from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world!")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world! from about page")

def contact(request):
    return HttpResponse("Hello, world! from contact page")