from django.contrib.auth.models import AbstractUser

from django.db import models

class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    contrasenya = models.CharField(max_length=128, default='admin')

    def __str__(self):
        return self.nom

