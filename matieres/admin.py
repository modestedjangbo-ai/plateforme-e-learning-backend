# Register your models here.
from django.contrib import admin
from .models import Matiere

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ("nom", "classe")
    list_filter = ("classe",)
    search_fields = ("nom",)