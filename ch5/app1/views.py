from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    h1 = "<h1>This is APP 1"
    return HttpResponse(h1)