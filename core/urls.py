from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/courses/', include('courses.urls')),

    path('api/enrollement/', include('enrollement.urls')),

    path('api/', include('accounts.urls')),

]