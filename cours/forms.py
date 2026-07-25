from django import forms
from .models import Cours


class CoursForm(forms.ModelForm):

    class Meta:

        model = Cours

        fields = [
            "titre",
            "classe",
            "matiere",
            "contenu",
            "fichier",
            "video",
    
        ]

        widgets = {

            "titre": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "classe": forms.Select(attrs={
             "class": "form-select"
            }),

            "description": forms.TextInput(attrs={
             "class": "form-control"
            }),

            "matiere": forms.Select(attrs={
                "class": "form-select"
            }),

            "contenu": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 8
            }),

            "video": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://www.youtube.com/..."
            }),
        }