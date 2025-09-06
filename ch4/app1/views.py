from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myFunction(request):
    return HttpResponse("Hello Django")


def home(request):
    return HttpResponse("This is Home Page")

def add(request):
    a= 22+2
    return HttpResponse(a)