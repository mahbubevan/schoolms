from django.contrib import admin
from . models import Staff
from clasub .models import Clasub

from student . gen_std_id import get_std_id
# Register your models here.


class ClasubInLine(admin.StackedInline):
    model = Clasub
    extra = 1

class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'role', 'is_active', 'hire_date',
    )
    list_editable = ('is_active',)
    list_display_links = ('id', 'first_name')
    list_per_page = 25
    search_fields = ('id', 'first_name', 'role')
    list_filter = ('hire_date', 'is_active')
    inlines = [ClasubInLine]

    def get_changeform_initial_data(self, request):
        return {'teacher_id': get_std_id()}


admin.site.register(Staff, StaffAdmin)
