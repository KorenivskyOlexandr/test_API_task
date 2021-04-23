from rest_framework import serializers
from datetime import date


def course_date_validation(start_date, end_date):
    if start_date >= end_date:
        raise serializers.ValidationError("end date must be bigger than start date")
    if start_date < date.today():
        raise serializers.ValidationError("start date must be bigger or same than today date")


def course_number_of_lectures_validation(number_of_lectures):
    if number_of_lectures <= 0:
        raise serializers.ValidationError("number of lectures must be positive digital")
