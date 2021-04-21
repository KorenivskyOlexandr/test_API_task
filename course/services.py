from .models import Course


def get_course_objects():
    return Course.objects.all()
