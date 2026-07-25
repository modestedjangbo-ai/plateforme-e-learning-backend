from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_eleve, name="dashboard_eleve"),

    path(
        "mes-cours/",
        views.mes_cours,
        name="mes_cours_eleve",
    ),

    path(
        "cours/<int:id>/",
        views.detail_cours,
        name="detail_cours_eleve",
    ),
]