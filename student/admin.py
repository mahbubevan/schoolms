from django.contrib import admin

from .models import Student
# Register your models here.
from . gen_std_id import get_std_id


class StudentModel(admin.ModelAdmin):
    list_display = ('student_id', 'first_name',
                    'last_name', 'family', 'is_active')
    list_editable = ('first_name', 'last_name', 'is_active')
    list_display_links = ('student_id',)
    search_fields = ('student_id',)
    list_filter = ('is_active',)
    list_per_page = 25

    def get_changeform_initial_data(self, request):
        return {'student_id': get_std_id()}


admin.site.register(Student, StudentModel)
