from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from comptes.decorators import eleve_required
from cours.models import Cours
from django.shortcuts import get_object_or_404

@login_required
@eleve_required
def dashboard_eleve(request):

    classe = request.user.profil.classe

    cours = Cours.objects.filter(classe=classe)

    nb_cours = cours.count()
    nb_pdf = cours.exclude(fichier="").count()
    nb_video = cours.exclude(video="").count()

    derniers_cours = cours.order_by("-date_publication")[:5]

    return render(
        request,
        "eleve/dashboard.html",
        {
            "classe": classe,
            "nb_cours": nb_cours,
            "nb_pdf": nb_pdf,
            "nb_video": nb_video,
            "derniers_cours": derniers_cours,
        },
    )




@login_required
@eleve_required
def mes_cours(request):

    classe = request.user.profil.classe

    cours = (
        Cours.objects
        .filter(classe=classe)
        .select_related("matiere", "enseignant")
        .order_by("matiere__nom", "titre")
    )

    return render(
        request,
        "eleve/mes_cours.html",
        {
            "cours": cours,
        },
    )


@login_required
@eleve_required
def detail_cours(request, id):

    cours = get_object_or_404(
        Cours,
        id=id,
        classe=request.user.profil.classe,
    )

    return render(
        request,
        "eleve/detail_cours.html",
        {
            "cours": cours,
        },
    )