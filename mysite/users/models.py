from django.db import models
from django.contrib.auth.models import AbstractUser
from distribuidores.models import Estado


class User(AbstractUser):
    estado = models.ForeignKey(Estado, blank=True, null=True, on_delete=models.CASCADE)