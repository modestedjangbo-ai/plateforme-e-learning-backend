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

'''class Classe(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    niveau = models.CharField(
        max_length=20,
        choices=[
            ("6e", "6e"),
            ("5e", "5e"),
            ("4e", "4e"),
            ("3e", "3e"),
        ],
    )
    salle = models.CharField(max_length=20, blank=True)'''