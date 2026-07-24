from django.db import models
from courses.models import Course  # On importe le modèle Course pour faire le lien

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name="Cours lié")
    title = models.CharField(max_length=200, verbose_name="Titre de la leçon")
    content = models.TextField(verbose_name="Contenu de la leçon")
    order = models.PositiveIntegerField(verbose_name="Ordre de la leçon")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order'] # Pour que les leçons s'affichent dans l'ordre que vous avez défini 
