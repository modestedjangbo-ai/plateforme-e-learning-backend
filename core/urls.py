from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),


    path(
        'api/',
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


    path(
        'api/contact/',
        include('contact.urls')
    ),
    path(
    'api/quiz/',
    include('quiz.urls')
),

]