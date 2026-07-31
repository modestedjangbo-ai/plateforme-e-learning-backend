from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer

from lessons.models import Lesson
from lessons.serializers import LessonSerializer

from accounts.models import User
from enrollement.models import Enrollment



class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer




@api_view(['GET'])
def course_lessons(request, id):

    lessons = Lesson.objects.filter(
        course_id=id
    )

    serializer = LessonSerializer(
        lessons,
        many=True
    )

    return Response(serializer.data)





@api_view(['GET'])
def admin_stats(request):

    nombre_etudiants = User.objects.filter(
        role="student"
    ).count()


    nombre_formateurs = User.objects.filter(
        role="teacher"
    ).count()


    nombre_cours = Course.objects.count()


    nombre_inscriptions = Enrollment.objects.count()



    return Response({

        "students": nombre_etudiants,

        "teachers": nombre_formateurs,

        "courses": nombre_cours,

        "enrollments": nombre_inscriptions

    })