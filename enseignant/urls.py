from django.urls import path
from . import views

urlpatterns = [
    # Tableau de bord enseignant
    path(
        "",
        views.dashboard_enseignant,
        name="dashboard_enseignant"
    ),

    # Liste des cours
    path(
    "mes-cours/",
    views.mes_cours,
    name="mes_cours_enseignant",
    ),

    # Nouveau cours
    path(
        "cours/nouveau/",
        views.nouveau_cours,
        name="nouveau_cours"
    ),

    # Voir un cours
    path(
        "cours/<int:cours_id>/",
        views.voir_cours,
        name="voir_cours"
    ),

    # Modifier un cours
    path(
        "cours/<int:cours_id>/modifier/",
        views.modifier_cours,
        name="modifier_cours"
    ),

    # Supprimer un cours
    path(
        "cours/<int:cours_id>/supprimer/",
        views.supprimer_cours,
        name="supprimer_cours"
    ),
]