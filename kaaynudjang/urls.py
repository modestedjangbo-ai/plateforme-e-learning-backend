from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("comptes/", include("comptes.urls")),
    path("enseignant/", include("enseignant.urls")),
    path("administration/", include("administration.urls")),
    path("eleve/", include("eleve.urls")),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)