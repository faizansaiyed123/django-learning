from django.shortcuts import render



def django_app(req):
    course_name = {'cname':'Django'}
    return render(req , 'course/django.html',context=course_name)