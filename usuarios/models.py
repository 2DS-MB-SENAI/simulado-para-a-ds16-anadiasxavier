from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuarios(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    REQUIRED_FIELDS = ['telefone']