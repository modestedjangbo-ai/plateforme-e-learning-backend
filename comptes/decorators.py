from functools import wraps
from django.shortcuts import redirect


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if (
            request.user.is_authenticated
            and hasattr(request.user, "profil")
            and request.user.profil.role == "admin"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("connexion")

    return wrapper


def enseignant_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if (
            request.user.is_authenticated
            and hasattr(request.user, "profil")
            and request.user.profil.role == "enseignant"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("connexion")

    return wrapper


def eleve_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if (
            request.user.is_authenticated
            and hasattr(request.user, "profil")
            and request.user.profil.role == "eleve"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("connexion")

    return wrapper