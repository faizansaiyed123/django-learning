from django import forms
from student.models import Profile

# class Registration(forms.Form):
#     first_name = forms.CharField(error_messages={'required':"Name is Required"})
#     email = forms.EmailField(error_messages={'required':"Email is Required"})
#     password = forms.CharField(
#         error_messages={'required':"Password is Required"},
#         widget=forms.PasswordInput(), 
#         max_length=100
#     )


class Registration(forms.ModelForm):
    confirm_password = forms.CharField()
    class Meta:
        model = Profile
        fields = ['name', 'email','password']
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}
        error_messages = {
            'name':{'required':'Name is Required'},
            'email':{'required':'Email is Required'},
            'password':{'required':'password is required'},
            }
        widgets = {
            'password':forms.PasswordInput
            }