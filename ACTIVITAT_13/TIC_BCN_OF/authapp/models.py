from django.contrib.auth.models import AbstractUser

from django.db import models

class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    ciutat = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

