# Register your models here.
from django.contrib import admin
from .models import Cours

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "matiere", "date_publication")
    list_filter = ("matiere",)
    search_fields = ("titre",)