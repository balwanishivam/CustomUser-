from django.contrib.auth.models import User
from django import forms
from .models import Myuser

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Myuser
        fields=['email','password','username','organisation_name','user_type']

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Myuser
        fields=['email','password','user_type']