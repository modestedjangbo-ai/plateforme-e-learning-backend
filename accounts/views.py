from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import RegisterSerializer, UserSerializer



# ==========================
# INSCRIPTION UTILISATEUR
# ==========================

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer



# ==========================
# CONNEXION UTILISATEUR
# ==========================

@api_view(['POST'])
def login_view(request):

    username = request.data.get("username")
    password = request.data.get("password")


    user = authenticate(
        username=username,
        password=password
    )


    if user is not None:

        refresh = RefreshToken.for_user(user)


        return Response({

            "refresh": str(refresh),

            "access": str(refresh.access_token),

            "username": user.username,

            "role": user.role

        })


    return Response(

        {
            "error": "Nom d'utilisateur ou mot de passe incorrect"
        },

        status=400

    )



# ==========================
# LISTE DES UTILISATEURS ADMIN
# ==========================

class UserListView(generics.ListAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer