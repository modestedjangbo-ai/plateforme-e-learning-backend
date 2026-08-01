from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CourseViewSet,
    admin_stats,
    teacher_stats
)



router = DefaultRouter()


router.register(
    '',
    CourseViewSet,
    basename='course'
)



urlpatterns = [


    path(
        '',
        include(router.urls)
    ),



    path(
        'admin/stats/',
        admin_stats,
        name='admin-stats'
    ),



    path(
        'teacher/stats/',
        teacher_stats,
        name='teacher-stats'
    ),

]