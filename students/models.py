#define database models that django converts into database tables itself
from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=30)
    cgpa = models.FloatField()

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}"
    