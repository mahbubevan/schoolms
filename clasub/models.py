from django.db import models
from staff . models import Staff
# Create your models here.


class Clasub(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    lession_time = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject
