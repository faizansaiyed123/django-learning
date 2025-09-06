from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    h1 = '<H1> This is APP 2 </H2>'
    return HttpResponse(h1)