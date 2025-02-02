from django.db import models

class Persona(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    edat = models.IntegerField()
    rol = models.CharField(max_length=50)
    curs = models.CharField(max_length=50)
    data_creacio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
