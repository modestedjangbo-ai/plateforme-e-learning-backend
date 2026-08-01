from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'role',
        'is_staff',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'Informations supplémentaires',
            {
                'fields': (
                    'role',
                )
            }
        ),
    )