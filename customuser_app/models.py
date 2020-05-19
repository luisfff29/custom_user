from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=128, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
