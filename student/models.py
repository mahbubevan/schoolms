from django.db import models
from family.models import Family

from staff.models import Staff
from clasub . models import Clasub
# Create your models here.


class Student(models.Model):
    clasub = models.ManyToManyField(Clasub)
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    note = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    student_id = models.CharField(max_length=200)

    def __str__(self):
        return self.student_id
