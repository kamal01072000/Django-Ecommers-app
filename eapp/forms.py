from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import User


class customuserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

    class Meta:
        model= User 
        fields = ['username','email','password1','password2']