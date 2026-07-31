from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import authenticate

from .serializers import RegisterSerializer
from .models import User



class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer





@api_view(['POST'])
def login_view(request):

    username = request.data.get('username')
    password = request.data.get('password')


    user = authenticate(
        username=username,
        password=password
    )


    if user is not None:

        return Response({

            "message": "Connexion réussie",

            "username": user.username,

            "role": user.role

        })


    return Response({

        "error": "Nom d'utilisateur ou mot de passe incorrect"

    }, status=400)