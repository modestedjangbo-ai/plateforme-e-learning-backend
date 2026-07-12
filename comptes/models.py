'''from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
'''
'''class Profil(models.Model):
    ROLES = [
        ("admin", "Administrateur"),
        ("enseignant", "Enseignant"),
        ("eleve", "Élève"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.user.username} ({self.role})" '''
from django.db import models
from django.contrib.auth.models import User


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

    photo = models.CharField(
    max_length=255,
    blank=True

    )

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.get_role_display()}"