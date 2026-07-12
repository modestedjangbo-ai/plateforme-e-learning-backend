# Create your models here.
from django.db import models
from matieres.models import Matiere

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    matiere = models.ForeignKey(
        Matiere,
        on_delete=models.CASCADE,
        related_name="cours"
    )
    contenu = models.TextField()
    fichier = models.FileField(
        upload_to="cours/pdf/",
        blank=True,
        null=True
    )
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_publication"]
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.titre