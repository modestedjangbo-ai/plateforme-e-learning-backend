from django import forms
from django.contrib.auth.models import User
from comptes.models import Profil
from classes.models import Classe
from matieres.models import Matiere 
from cours.models import Cours


class EnseignantForm(forms.ModelForm):
    # Mot de passe saisi lors de la création
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "username": "Nom d'utilisateur",
            "email": "Adresse e-mail",
        }

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }



class EleveForm(forms.ModelForm):
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    classe = forms.ModelChoiceField(
        queryset=Classe.objects.all().order_by("nom"),
        label="Classe",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "username": "Nom d'utilisateur",
            "email": "Adresse e-mail",
        }

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }    

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ["nom"]

        widgets = {
            "nom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex : 6e A, 5e B, 3e C..."
                }
            ),
        } 

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ["nom", "classe"]

        widgets = {
            "nom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nom de la matière"
                }
            ),
            "classe": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }
#Cours form
class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = [
            "classe",
            "matiere",
            "titre",
            "description",
            "contenu",
            "fichier",
            "video",
        ]

        widgets = {
            "classe": forms.Select(attrs={"class": "form-select"}),
            "matiere": forms.Select(attrs={"class": "form-select"}),

            "titre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Titre du cours"
            }),

            "description": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Description courte"
            }),

            "contenu": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Contenu du cours"
            }),

            "fichier": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "video": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://youtube.com/..."
            }),
        }        