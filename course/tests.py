from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course
from datetime import date, timedelta


class CourseTests(APITestCase):
    def setUp(self):
        self.url = reverse("course-list")
        self.start_date = date.today() + timedelta(days=5)
        self.end_date = self.start_date + timedelta(days=25)
        self.data = {
            "name": "Python course",
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_lectures": 50}

    def test_post_create_course(self):
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, "Python course")

    def test_get_course_list(self):
        self.client.post(self.url, self.data, format="json")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_course(self):
        self.client.post(self.url, self.data, format="json")
        self.assertEqual(Course.objects.get().name, "Python course")
        new_data = self.data
        new_data["name"] = "DevOps course"
        self.client.put(reverse("course-detail", kwargs={"pk": 1}), new_data, format="json")
        self.assertEqual(Course.objects.get().name, "DevOps course")

    def test_patch_course(self):
        self.client.post(self.url, self.data, format="json")
        self.assertEqual(Course.objects.get().name, "Python course")
        new_data = self.data
        new_data["name"] = "DevOps course"
        self.client.patch(reverse("course-detail", kwargs={"pk": 1}), new_data, format="json")
        self.assertEqual(Course.objects.get().name, "DevOps course")

    def test_delete_course(self):
        self.client.post(self.url, self.data, format="json")
        self.assertEqual(Course.objects.count(), 1)
        self.client.delete(reverse("course-detail", kwargs={"pk": 1}), format="json")
        self.assertEqual(Course.objects.count(), 0)

    def test_start_date_validation(self):
        wrong_data = self.data
        wrong_data["start_date"] = date.today() - timedelta(days=5)
        response = self.client.post(self.url, wrong_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_end_date_validation(self):
        wrong_data = self.data
        wrong_data["end_date"] = self.data.get("start_date") - timedelta(days=5)
        response = self.client.post(self.url, wrong_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_number_of_lectures_validation(self):
        wrong_data = self.data
        wrong_data["number_of_lectures"] = 0
        response = self.client.post(self.url, wrong_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        wrong_data["number_of_lectures"] = -10
        response = self.client.post(self.url, wrong_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
