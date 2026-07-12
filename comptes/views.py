# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def connexion(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard")

        return render(request, "comptes/login.html", {
            "erreur": "Nom d'utilisateur ou mot de passe incorrect."
        })

    return render(request, "comptes/login.html")
#Deconnexion
def deconnexion(request):
    logout(request)
    return redirect("accueil")
#Tableau de bord
@login_required
def tableau_de_bord(request):
    return render(request, "comptes/dashboard.html")