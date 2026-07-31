from rest_framework import serializers
from courses.models import Course


class DashboardCourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = [
            'id',
            'title',
            'description'
        ]