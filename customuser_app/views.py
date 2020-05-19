from django.shortcuts import render, reverse
from customuser_app.models import MyUser
from customuser_app.forms import MyUserForm, LoginForm

from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    users_list = MyUser.objects.all()
    return render(request, 'index.html', {'users_list': users_list})


def signupform(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = MyUser.objects.create_user(
                username=data['username'], password=data['password'], display_name=data['display_name'], is_staff=True, is_superuser=True)
            usuario.save()
        return HttpResponseRedirect(reverse('home'))

    form = MyUserForm()
    return render(request, 'signup.html', {'form': form})


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = authenticate(
                request, username=data['username'], password=data['password'])
            if usuario:
                login(request, usuario)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'login.html', {'form': form})
