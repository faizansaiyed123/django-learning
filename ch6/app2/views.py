from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def my_app2(req):
    return HttpResponse(f"<h1>Learn Django My_App2</h1>")