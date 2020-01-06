from django.db import models

# Create your models here.


class Staff(models.Model):
    Lecturer = 'LR'
    Assistant_Professor = 'AP'
    Professor  = 'PF'

    staff_role = [
        (Lecturer,'Lecturer'),
        (Assistant_Professor,'Assistant Professor'),
        (Professor,'Professor'),
    ]


    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default='new')
    password = models.CharField(max_length=200,default='teacher')
    teacher_id = models.CharField(max_length=200,default='1234')
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    role = models.CharField(choices=staff_role,max_length=200,default=Lecturer)
    description = models.TextField(blank=True)
    hire_date = models.DateField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return self.first_name + self.last_name
