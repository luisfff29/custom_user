from django.shortcuts import render
from customuser_app.models import MyUser
from customuser_app.forms import MyUserForm


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
        return render(request, 'index.html', {'usuario': usuario})

    form = MyUserForm()
    return render(request, 'signup.html', {'form': form})
