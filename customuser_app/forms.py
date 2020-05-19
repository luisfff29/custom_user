from django import forms
from customuser_app.models import MyUser


class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = MyUser
        fields = ['username', 'password', 'display_name']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput())
