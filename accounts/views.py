from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class ProfileUpdateView(generics.UpdateAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
