from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Enrollment
from courses.serializers import CourseSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_dashboard(request):

    student = request.user


    enrollments = Enrollment.objects.filter(
        student=student
    )


    courses = []


    for enrollment in enrollments:

        courses.append(
            enrollment.course
        )


    serializer = CourseSerializer(
        courses,
        many=True
    )


    return Response({

        "username": student.username,

        "courses": serializer.data

    })