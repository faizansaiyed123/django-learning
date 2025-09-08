from django.shortcuts import render,redirect
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile
def success(req):
    return render(req, "student/success.html")


def register(req):
    if req.method =='POST':
        form = Registration(req.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            cpw = form.cleaned_data['confirm_password']
            pr = Profile(name=nm, email=em, password=pw)
            pr.save()
            return redirect("success")
    else:
        form = Registration()
    return render(req , "student/register.html", {'form':form})


