from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard_admin"),

    path(
        "enseignants/",
        views.liste_enseignants,
        name="liste_enseignants",
    ),
    path(
    "enseignants/<int:id>/modifier/",
    views.modifier_enseignant,
    name="modifier_enseignant",
    ),
    path(
    "enseignants/ajouter/",
    views.ajouter_enseignant,
    name="ajouter_enseignant",
    ),
    path(
    "enseignants/<int:id>/supprimer/",
    views.supprimer_enseignant,
    name="supprimer_enseignant",
    ),
     path(
    "eleves/",
    views.liste_eleves,
    name="liste_eleves",
),

path(
    "eleves/ajouter/",
    views.ajouter_eleve,
    name="ajouter_eleve",
),

path(
    "eleves/<int:id>/modifier/",
    views.modifier_eleve,
    name="modifier_eleve",
),

path(
    "eleves/<int:id>/supprimer/",
    views.supprimer_eleve,
    name="supprimer_eleve",
),

path("classes/", views.liste_classes, name="liste_classes"),
path("classes/ajouter/", views.ajouter_classe, name="ajouter_classe"),
path("classes/<int:id>/modifier/", views.modifier_classe, name="modifier_classe"),
path("classes/<int:id>/supprimer/", views.supprimer_classe, name="supprimer_classe"),
path("matieres/", views.liste_matieres, name="liste_matieres"),
path("matieres/ajouter/", views.ajouter_matiere, name="ajouter_matiere"),
path("matieres/<int:id>/modifier/", views.modifier_matiere, name="modifier_matiere"),
path("matieres/<int:id>/supprimer/", views.supprimer_matiere, name="supprimer_matiere"),

path("cours/", views.liste_cours, name="liste_cours"),
path("cours/ajouter/", views.ajouter_cours, name="ajouter_cours"),
path("cours/<int:id>/modifier/", views.modifier_cours, name="modifier_cours"),
path("cours/<int:id>/supprimer/", views.supprimer_cours, name="supprimer_cours"),

path(
    "statistiques/",
    views.statistiques,
    name="statistiques",
),
#les dashboards pour chaque rôle

]