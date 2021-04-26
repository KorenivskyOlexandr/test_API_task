from rest_framework import permissions, viewsets
from .serializers import CourseSerializer
from .services import get_course_objects
from .filters import CourseFilter


class CourseListView(viewsets.ModelViewSet):
    queryset = get_course_objects()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializer
    filter_class = CourseFilter
