from django.urls import path
from course.views import django_app
urlpatterns = [
    path("dj/", django_app),
    ]