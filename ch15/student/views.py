from django.shortcuts import render
from student.forms import Registration, Login
# Create your views here.

def registration(req):
    fm = Registration()
    return render(req , "student/registration.html",{'form':fm})


def login(req):
    fm = Login()
    return render(req , "student/login.html",{'form':fm})