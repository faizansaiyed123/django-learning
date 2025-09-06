from django.urls import path
from  course.views import course


urlpatterns = [
    path('php/', course),
]
