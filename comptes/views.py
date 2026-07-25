from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def connexion(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            try:
                role = user.profil.role

            except AttributeError:

                logout(request)

                return render(
                    request,
                    "comptes/login.html",
                    {
                        "erreur": "Aucun profil n'est associé à cet utilisateur."
                    }
                )

            if role == "admin":
                return redirect("dashboard_admin")

            elif role == "enseignant":
                return redirect("dashboard_enseignant")

            elif role == "eleve":
                return redirect("dashboard_eleve")

            logout(request)

            return render(
                request,
                "comptes/login.html",
                {
                    "erreur": "Rôle utilisateur invalide."
                }
            )

        return render(
            request,
            "comptes/login.html",
            {
                "erreur": "Nom d'utilisateur ou mot de passe incorrect."
            }
        )

    return render(request, "comptes/login.html")


def deconnexion(request):
    logout(request)
    return redirect("accueil")


@login_required
def tableau_de_bord(request):
    return redirect("connexion")