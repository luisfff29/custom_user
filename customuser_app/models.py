from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    homepage = models.URLField()
    display_name = models.CharField(max_length=128, null=True, blank=True)
    age = models.IntegerField()
