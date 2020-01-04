from django.db import models

# Create your models here.


class Family(models.Model):
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    father_phone = models.CharField(max_length=50, blank=True)
    mother_phone = models.CharField(max_length=50, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.father_name
