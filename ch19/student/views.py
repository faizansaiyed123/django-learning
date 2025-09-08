from django.shortcuts import render
from student.forms import Registration


def registration(req):
    form = Registration()
    return render(req , "student/registration.html", {'form':form})