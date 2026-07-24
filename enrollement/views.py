from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Enrollment
from .serializers import EnrollmentSerializer


@api_view(['POST'])
def enroll_course(request):

    serializer = EnrollmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Inscription réussie",
            "data": serializer.data
        })

    return Response(serializer.errors, status=400)