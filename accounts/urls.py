from django.urls import path

from .views import (
    RegisterView,
    login_view,
    UserListView
)


urlpatterns = [

    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),


    path(
        'connexion/',
        login_view,
        name='connexion'
    ),


    path(
        'users/',
        UserListView.as_view(),
        name='users'
    ),

]