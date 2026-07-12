# Create your models here.
from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['nom']
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.nom