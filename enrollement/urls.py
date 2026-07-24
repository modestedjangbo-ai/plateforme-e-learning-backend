from django.urls import path
from .views import enroll_course


urlpatterns = [
    path('enroll/', enroll_course),
]