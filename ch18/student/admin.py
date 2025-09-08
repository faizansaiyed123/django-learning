from django.contrib import admin
from student.models import Profile , Result

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'city','roll']



