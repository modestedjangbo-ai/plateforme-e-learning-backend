from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),


    path(
        'api/register/',
        include('accounts.urls')
    ),


    path(
        'api/courses/',
        include('courses.urls')
    ),


    path(
        'api/enrollement/',
        include('enrollement.urls')
    ),


    path(
        'api/lessons/',
        include('lessons.urls')
    ),


    # API CONTACT
    path(
        'api/contact/',
        include('contact.urls')
    ),

]