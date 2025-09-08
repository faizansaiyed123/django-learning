from django.db import models



class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=255)
    roll = models.IntegerField()


    # def __str__(self):
    #     return str(self.roll)


class Result(models.Model):
    stu_class = models.CharField(max_length=25)
    marks = models.IntegerField()


    # def __str__(self):
    #     return self.stu_class
