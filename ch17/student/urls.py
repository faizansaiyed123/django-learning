from django.urls import path
from student.views import all_data, single_data

urlpatterns = [
    path("all/", all_data, name="all_data"),
    path("one/", single_data, name="all_data"),
    ]