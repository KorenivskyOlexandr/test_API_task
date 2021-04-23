from rest_framework import serializers
from .models import Course
from .validation import course_date_validation, course_number_of_lectures_validation


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def validate(self, data):
        course_date_validation(data.get("start_date"), data.get("end_date"))
        course_number_of_lectures_validation(data.get("number_of_lectures"))
        return data
