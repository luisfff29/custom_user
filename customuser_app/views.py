from django.shortcuts import render
from customuser_app.models import MyUser
from customuser_app.forms import MyUserForm


# Create your views here.
def index(request):
    users_list = MyUser.objects.all()
    return render(request, 'index.html', {'users_list': users_list})


def signupform(request):
    form = MyUserForm()
    return render(request, 'signup.html', {'form': form})
