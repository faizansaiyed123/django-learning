from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=30)