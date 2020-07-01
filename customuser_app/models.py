from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    homepage = models.URLField(null=True, blank=True)
    display_name = models.CharField(max_length=128, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    # https://stackoverflow.com/questions/40396049/cannot-create-super-user-in-django
    REQUIRED_FIELDS = ['age']
