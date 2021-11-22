from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class uzytkownik(AbstractUser):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)