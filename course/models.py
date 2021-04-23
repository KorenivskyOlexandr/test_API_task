from django.db import models
from .validation import course_date_validation, course_number_of_lectures_validation


class Course(models.Model):
    name = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_lectures = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        course_date_validation(self.start_date, self.end_date)
        course_number_of_lectures_validation(self.number_of_lectures)
        super(Course, self).save(*args, **kwargs)
