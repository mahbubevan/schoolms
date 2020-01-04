from django.db import models

# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    hire_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.first_name + self.last_name
