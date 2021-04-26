from rest_framework import routers
from .api import CourseListView

router = routers.DefaultRouter()
router.register("api/courses", CourseListView, 'course')

urlpatterns = router.urls
