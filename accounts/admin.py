from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_superuser",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Informations supplémentaires", {
            "fields": ("role", "created_at"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informations supplémentaires", {
            "fields": ("email", "role"),
        }),
    )

    readonly_fields = ("created_at",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)