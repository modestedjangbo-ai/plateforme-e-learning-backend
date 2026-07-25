from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cours.forms import CoursForm


@login_required
def nouveau_cours(request):

    if request.method == "POST":

        form = CoursForm(request.POST, request.FILES)

        if form.is_valid():

            cours = form.save(commit=False)

            cours.enseignant = request.user

            cours.save()

            return redirect("dashboard_enseignant")

    else:
        form = CoursForm()

    return render(
        request,
        "enseignant/nouveau_cours.html",
        {
            "form": form
        }
    )