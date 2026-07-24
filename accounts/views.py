from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


User = get_user_model()



@csrf_exempt
def register_view(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")


        if User.objects.filter(email=email).exists():

            return JsonResponse(
                {
                    "message": "Cet email existe déjà"
                },
                status=400
            )


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        return JsonResponse(
            {
                "message": "Compte créé avec succès",
                "username": user.username,
                "email": user.email
            },
            status=201
        )



    return JsonResponse(
        {
            "message": "Méthode non autorisée"
        },
        status=405
    )






@csrf_exempt
def login_view(request):

    if request.method == "POST":


        data = json.loads(request.body)


        email = data.get("email")
        password = data.get("password")



        try:

            user = User.objects.get(
                email=email
            )


        except User.DoesNotExist:


            return JsonResponse(
                {
                    "message": "Email incorrect"
                },
                status=401
            )



        if user.check_password(password):


            return JsonResponse(
                {
                    "message": "Connexion réussie",
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                },
                status=200
            )



        return JsonResponse(
            {
                "message": "Mot de passe incorrect"
            },
            status=401
        )



    return JsonResponse(
        {
            "message": "Méthode non autorisée"
        },
        status=405
    )