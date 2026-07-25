from django.db import models
from django.contrib.auth.models import User
from classes.models import Classe


class Profil(models.Model):

    ADMIN = "admin"
    ENSEIGNANT = "enseignant"
    ELEVE = "eleve"

    ROLES = [
        (ADMIN, "Administrateur"),
        (ENSEIGNANT, "Enseignant"),
        (ELEVE, "Élève"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profil"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default=ELEVE
    )

    telephone = models.CharField(
        max_length=20,
        blank=True
    )

    
    photo = models.ImageField(
    upload_to="profils/",
    blank=True,
    null=True,
    default="profils/default.png"
    )
    classe = models.ForeignKey(
    Classe,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="eleves"
)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.get_role_display()}"