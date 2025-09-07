from django.db import models


class Profile(models.Model):
    name =  models.CharField(max_length=70)
    email = models.EmailField(max_length=80)
    city = models.CharField(max_length=80)
    roll = models.IntegerField()
    state = models.CharField(max_length=30)
    comment = models.CharField(max_length=100, default='Nothing')
    
    
    
