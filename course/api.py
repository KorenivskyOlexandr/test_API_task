from rest_framework import viewsets, permissions
from .serializers import CourseSerializer
from .services import get_course_objects


class CourseViewSet(viewsets.ModelViewSet):
    queryset = get_course_objects()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializer
