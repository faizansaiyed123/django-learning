from django.contrib import admin
from student.models import Profile


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'email','city']

# admin.site.register(Profile,ProfileAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','city']

    