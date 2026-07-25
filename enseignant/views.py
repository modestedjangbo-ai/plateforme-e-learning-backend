from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from cours.forms import CoursForm
from cours.models import Cours


@login_required
def dashboard_enseignant(request):
    cours_queryset = Cours.objects.filter(enseignant=request.user)

    nb_cours = cours_queryset.count()
    nb_pdf = cours_queryset.exclude(fichier="").count()
    nb_video = cours_queryset.exclude(video="").count()
    derniers_cours = cours_queryset.order_by("-date_publication")[:5]

    return render(
        request,
        "enseignant/dashboard.html",
        {
            "nb_cours": nb_cours,
            "nb_pdf": nb_pdf,
            "nb_video": nb_video,
            "derniers_cours": derniers_cours,
        },
    )


@login_required
def mes_cours(request):
    cours = (
        Cours.objects.filter(enseignant=request.user)
        .order_by("-date_publication")
    )

    return render(
        request,
        "enseignant/mes_cours.html",
        {
            "cours": cours,
        },
    )


@login_required
def nouveau_cours(request):
    if request.method == "POST":
        form = CoursForm(request.POST, request.FILES)

        if form.is_valid():
            cours = form.save(commit=False)
            cours.enseignant = request.user
            cours.save()

            messages.success(
                request,
                "Le cours a été créé avec succès."
            )

            return redirect("mes_cours")

    else:
        form = CoursForm()

    return render(
        request,
        "enseignant/nouveau_cours.html",
        {
            "form": form,
        },
    )


@login_required
def voir_cours(request, cours_id):
    cours = get_object_or_404(
        Cours,
        id=cours_id,
        enseignant=request.user,
    )

    video_embed = None

    if cours.video:
        url = cours.video.strip()

        if "watch?v=" in url:
            video_embed = url.replace("watch?v=", "embed/")

        elif "youtu.be/" in url:
            video_embed = url.replace(
                "https://youtu.be/",
                "https://www.youtube.com/embed/",
            )

    return render(
        request,
        "enseignant/voir_cours.html",
        {
            "cours": cours,
            "video_embed": video_embed,
        },
    )


@login_required
def modifier_cours(request, cours_id):
    cours = get_object_or_404(
        Cours,
        id=cours_id,
        enseignant=request.user,
    )

    if request.method == "POST":
        form = CoursForm(
            request.POST,
            request.FILES,
            instance=cours,
        )

        if form.is_valid():
            cours = form.save(commit=False)
            cours.enseignant = request.user
            cours.save()

            messages.success(
                request,
                "Le cours a été modifié avec succès."
            )

            return redirect("mes_cours_enseignant")

    else:
        form = CoursForm(instance=cours)

    return render(
        request,
        "enseignant/modifier_cours.html",
        {
            "form": form,
            "cours": cours,
        },
    )


@login_required
def supprimer_cours(request, cours_id):
    cours = get_object_or_404(
        Cours,
        id=cours_id,
        enseignant=request.user,
    )

    if request.method == "POST":
        titre = cours.titre
        cours.delete()

        messages.success(
            request,
            f'Le cours "{titre}" a été supprimé avec succès.'
        )

        return redirect("mes_cours_enseignant")

    return render(
        request,
        "enseignant/supprimer_cours.html",
        {
            "cours": cours,
        },
    )