from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('learner', 'Learner'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('manager', 'Manager'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username