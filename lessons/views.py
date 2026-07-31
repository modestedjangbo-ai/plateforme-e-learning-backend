from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer



class LessonListCreateView(generics.ListCreateAPIView):

    queryset = Lesson.objects.all()

    serializer_class = LessonSerializer