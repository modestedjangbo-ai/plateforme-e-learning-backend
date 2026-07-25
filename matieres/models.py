from django.db import models
from classes.models import Classe


class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    classe = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE,
        related_name="matieres"
    )

    class Meta:
        ordering = ["classe", "nom"]
        verbose_name = "Matière"
        verbose_name_plural = "Matières"

        constraints = [
            models.UniqueConstraint(
                fields=["nom", "classe"],
                name="unique_matiere_par_classe"
            )
        ]

    def __str__(self):
        return f"{self.nom} ({self.classe})"