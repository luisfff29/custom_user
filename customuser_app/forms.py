from django import forms
from customuser_app.models import MyUser


class MyUserForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = '__all__'
