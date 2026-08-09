from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    QuizViewSet,
    QuestionViewSet
)



router = DefaultRouter()


router.register(
    '',
    QuizViewSet,
    basename='quiz'
)


router.register(
    'questions',
    QuestionViewSet,
    basename='question'
)



urlpatterns = [

    path(
        '',
        include(router.urls)
    )

]