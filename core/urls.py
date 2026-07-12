from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
     path("classe/<int:classe_id>/", views.detail_classe, name="detail_classe"),
     path("matiere/<int:matiere_id>/", views.detail_matiere, name="detail_matiere"),
     path("cours/<int:cours_id>/", views.detail_cours, name="detail_cours"),
     path("recherche/", views.recherche, name="recherche"),
]