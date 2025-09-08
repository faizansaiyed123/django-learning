from django.shortcuts import render
from student.models  import Profile


def all_data(req):
    all_students = Profile.objects.all()
    return render(req , "student/all.html", {'student':all_students})



def single_data(req):
    # single_stu = Profile.objects.get(pk=1)
    # single_stu = Profile.objects.get(id=1)
    single_stu = Profile.objects.get(name='faizan')
    return render(req , "student/single.html", {'student':single_stu})