from django.db import models
from django.contrib.auth.models import User
from classes.models import Classe
from matieres.models import Matiere


class Cours(models.Model):

    enseignant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cours",
    )
    
    

    titre = models.CharField(max_length=200)

    description = models.CharField(
        max_length=255,
        blank=True
    )

    matiere = models.ForeignKey(
        Matiere,
        on_delete=models.CASCADE,
        related_name="cours"
    )

    classe = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE,
        related_name="cours",
    )
        
    

    contenu = models.TextField()

    fichier = models.FileField(
        upload_to="cours/pdf/",
        blank=True,
        null=True
    )

    video = models.URLField(
        blank=True,
        null=True,
        help_text="Lien YouTube (facultatif)"
    )

    date_publication = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_publication"]
        verbose_name = "Cours"
        verbose_name_plural = "Cours"
        constraints = [
            models.UniqueConstraint(
                fields=["titre", "classe", "matiere"],
                name="unique_cours_par_classe"
            )
        ]

    def __str__(self):
        return self.titre