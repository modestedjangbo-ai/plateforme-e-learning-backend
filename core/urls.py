from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Bienvenue sur l'API de la plateforme e-learning",
        "status": "success"
    })


urlpatterns = [
    # Accueil
    path("", home, name="home"),

    # Administration Django
    path("admin/", admin.site.urls),

    # Comptes / authentification
    path("api/", include("accounts.urls")),

    # Cours
    path("api/courses/", include("courses.urls")),

    # Inscriptions
    path("api/enrollement/", include("enrollement.urls")),

    # Leçons
    path("api/lessons/", include("lessons.urls")),
]