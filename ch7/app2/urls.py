from django.urls import path
from  app2.views import app2


urlpatterns = [
    path('app2/', app2),
]
