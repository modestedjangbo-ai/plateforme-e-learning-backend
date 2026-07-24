from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du cours")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to="courses/", blank=True, null=True)
    teacher = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    verbose_name="Enseignant"
)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title