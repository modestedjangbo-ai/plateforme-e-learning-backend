from urllib import request

from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from comptes.decorators import admin_required, enseignant_required
import cours
from .forms import EnseignantForm
from django.contrib import messages
from classes.models import Classe
from .forms import EnseignantForm, EleveForm, ClasseForm
from matieres.models import Matiere
from .forms import MatiereForm
from cours.models import Cours
from .forms import CoursForm

@login_required
@admin_required
def dashboard(request):
    return render(request, "administration/dashboard.html")


@login_required
@admin_required
def liste_enseignants(request):
    enseignants = User.objects.filter(
        profil__role="enseignant"
    ).order_by(
        "last_name",
        "first_name"
    )

    return render(
        request,
        "administration/enseignants.html",
        {
            "enseignants": enseignants
        },
    )
@login_required
@admin_required
def modifier_enseignant(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    enseignant = get_object_or_404(User, id=id)

    if request.method == "POST":
        form = EnseignantForm(request.POST, instance=enseignant)

        if form.is_valid():
            user = form.save(commit=False)

            # Modifier le mot de passe uniquement s'il est renseigné
            password = form.cleaned_data.get("password")
            if password:
                user.set_password(password)

            user.save()
            messages.success(
            request,
            "Les informations de l'enseignant ont été mises à jour avec succès."
            )

            return redirect("liste_enseignants")

    else:
        form = EnseignantForm(instance=enseignant)

    return render(
        request,
        "administration/modifier_enseignant.html",
        {
            "form": form,
            "enseignant": enseignant,
        },
    )

@login_required
@admin_required
def ajouter_enseignant(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    if request.method == "POST":
        form = EnseignantForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Chiffrement du mot de passe
            user.set_password(form.cleaned_data["password"])

            user.save()

            # Attribution automatique du rôle
            user.profil.role = "enseignant"
            user.profil.save()
            messages.success(
            request,
            f"L'enseignant {user.first_name} {user.last_name} a été ajouté avec succès."
)

            return redirect("liste_enseignants")

    else:
        form = EnseignantForm()

    return render(
        request,
        "administration/ajouter_enseignant.html",
        {"form": form},
    )

@login_required
@admin_required
def supprimer_enseignant(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    enseignant = get_object_or_404(User, id=id)

    if request.method == "POST":
        nom_complet = f"{enseignant.first_name} {enseignant.last_name}"

        enseignant.delete()

        messages.success(
            request,
            f"L'enseignant {nom_complet} a été supprimé avec succès."
        )

        return redirect("liste_enseignants")

    return render(
        request,
        "administration/supprimer_enseignant.html",
        {"enseignant": enseignant},
    )
#liste des élèves
@login_required
def liste_eleves(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    eleves = User.objects.filter(
        profil__role="eleve"
    ).order_by("last_name", "first_name")

    return render(
        request,
        "administration/eleves.html",
        {"eleves": eleves},
    )
# Ajouter un élève
@login_required
def ajouter_eleve(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    if request.method == "POST":
        form = EleveForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data["password"])
            user.save()

            profil = user.profil
            profil.role = "eleve"
            profil.classe = form.cleaned_data["classe"]
            profil.save()

            messages.success(
                request,
                f"L'élève {user.first_name} {user.last_name} a été ajouté avec succès."
            )

            return redirect("liste_eleves")

    else:
        form = EleveForm()

    return render(
        request,
        "administration/ajouter_eleve.html",
        {"form": form},
    )
# Modifier un élève
@login_required
def modifier_eleve(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    eleve = get_object_or_404(User, id=id)

    if request.method == "POST":
        form = EleveForm(request.POST, instance=eleve)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data["password"])
            user.save()

            profil = user.profil
            profil.classe = form.cleaned_data["classe"]
            profil.save()

            messages.success(
                request,
                "Les informations de l'élève ont été mises à jour."
            )

            return redirect("liste_eleves")

    else:
        initial = {
            "classe": eleve.profil.classe,
        }

        form = EleveForm(
            instance=eleve,
            initial=initial,
        )

    return render(
        request,
        "administration/modifier_eleve.html",
        {
            "form": form,
            "eleve": eleve,
        },
    )
# Supprimer un élève
@login_required
def supprimer_eleve(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    eleve = get_object_or_404(User, id=id)

    if request.method == "POST":
        nom = f"{eleve.first_name} {eleve.last_name}"

        eleve.delete()

        messages.success(
            request,
            f"L'élève {nom} a été supprimé avec succès."
        )

        return redirect("liste_eleves")

    return render(
        request,
        "administration/supprimer_eleve.html",
        {"eleve": eleve},
    )
# Liste des classes
@login_required
def liste_classes(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    classes = Classe.objects.all()

    return render(
        request,
        "administration/classes.html",
        {"classes": classes},
    )
#Ajouter une classe
@login_required
def ajouter_classe(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    if request.method == "POST":
        form = ClasseForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "La classe a été ajoutée avec succès."
            )

            return redirect("liste_classes")

    else:
        form = ClasseForm()

    return render(
        request,
        "administration/ajouter_classe.html",
        {"form": form},
    )
# Modifier une classe
@login_required
def modifier_classe(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    classe = get_object_or_404(Classe, id=id)

    if request.method == "POST":
        form = ClasseForm(request.POST, instance=classe)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "La classe a été modifiée avec succès."
            )

            return redirect("liste_classes")

    else:
        form = ClasseForm(instance=classe)

    return render(
        request,
        "administration/modifier_classe.html",
        {
            "form": form,
            "classe": classe,
        },
    )
# Supprimer une classe
@login_required
def supprimer_classe(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    classe = get_object_or_404(Classe, id=id)

    if request.method == "POST":
        classe.delete()

        messages.success(
            request,
            "La classe a été supprimée avec succès."
        )

        return redirect("liste_classes")

    return render(
        request,
        "administration/supprimer_classe.html",
        {"classe": classe},
    )
# Liste des matières
@login_required
def liste_matieres(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    matieres = Matiere.objects.select_related("classe").all()

    return render(
        request,
        "administration/matieres.html",
        {"matieres": matieres},
    )


@login_required
def ajouter_matiere(request):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    if request.method == "POST":
        form = MatiereForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "La matière a été ajoutée avec succès.")
            return redirect("liste_matieres")
    else:
        form = MatiereForm()

    return render(
        request,
        "administration/ajouter_matiere.html",
        {"form": form},
    )


@login_required
def modifier_matiere(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    matiere = get_object_or_404(Matiere, id=id)

    if request.method == "POST":
        form = MatiereForm(request.POST, instance=matiere)

        if form.is_valid():
            form.save()
            messages.success(request, "La matière a été modifiée avec succès.")
            return redirect("liste_matieres")
    else:
        form = MatiereForm(instance=matiere)

    return render(
        request,
        "administration/modifier_matiere.html",
        {
            "form": form,
            "matiere": matiere,
        },
    )


@login_required
def supprimer_matiere(request, id):
    if request.user.profil.role != "admin":
        return HttpResponseForbidden("Accès réservé à l'administrateur.")

    matiere = get_object_or_404(Matiere, id=id)

    if request.method == "POST":
        matiere.delete()
        messages.success(request, "La matière a été supprimée avec succès.")
        return redirect("liste_matieres")

    return render(
        request,
        "administration/supprimer_matiere.html",
        {"matiere": matiere},
    )

# Liste des cours

def liste_cours(request):
    cours = Cours.objects.select_related(
        "enseignant",
        "classe",
        "matiere"
    ).all()

    return render(
        request,
        "administration/cours.html",
        {"cours": cours}
    )


def ajouter_cours(request):
    if request.method == "POST":
        form = CoursForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("liste_cours")
    else:
        form = CoursForm()

    return render(
        request,
        "administration/ajouter_cours.html",
        {"form": form}
    )


def modifier_cours(request, id):
    cours = get_object_or_404(Cours, id=id)

    if request.method == "POST":
        form = CoursForm(
            request.POST,
            request.FILES,
            instance=cours
        )

        if form.is_valid():
            cours = form.save(commit=False)
            cours.enseignant = request.user
            cours.save()
        
            return redirect("liste_cours")
    else:
        form = CoursForm(instance=cours)

    return render(
        request,
        "administration/modifier_cours.html",
        {
            "form": form,
            "cours": cours
        }
    )


def supprimer_cours(request, id):
    cours = get_object_or_404(Cours, id=id)

    if request.method == "POST":
        cours.delete()
        return redirect("liste_cours")

    return render(
        request,
        "administration/supprimer_cours.html",
        {"cours": cours}
    )

@login_required
@admin_required
def statistiques(request):
    return render(request, "administration/statistiques.html")