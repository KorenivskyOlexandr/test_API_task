from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_lectures = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
