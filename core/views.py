# Create your views here.
from django.shortcuts import render, get_object_or_404
#from django.shortcuts import render
from classes.models import Classe
from matieres.models import Matiere
from cours.models import Cours
from django.db.models import Q
#from blog.models import Article

def accueil(request):

    classes = Classe.objects.all()

    derniers_cours = Cours.objects.order_by("-date_publication")[:6]

    context = {
        "classes": classes,
        "derniers_cours": derniers_cours,

        "nb_classes": Classe.objects.count(),
        "nb_matieres": Matiere.objects.count(),
        "nb_cours": Cours.objects.count(),
    }

    return render(request, "core/accueil.html", context)

def detail_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    matieres = Matiere.objects.filter(classe=classe)

    return render(request, "core/detail_classe.html", {
        "classe": classe,
        "matieres": matieres
    })
def detail_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    cours = Cours.objects.filter(matiere=matiere)

    return render(request, "core/detail_matiere.html", {
        "matiere": matiere,
        "cours": cours,
    })
def detail_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)

    return render(request, "core/detail_cours.html", {
        "cours": cours
    })
def recherche(request):
    query = request.GET.get("q", "")
    resultats = []

    if query:
        resultats = Cours.objects.filter(
            Q(titre__icontains=query) |
            Q(contenu__icontains=query)
        )

    return render(request, "core/recherche.html", {
        "query": query,
        "resultats": resultats,
    })