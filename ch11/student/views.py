from django.shortcuts import render
from student.models import Profile
# Create your views here.

def all_data(req):
    all_students = Profile.objects.all()
    return render(req,"student/all.html", {'students':all_students})