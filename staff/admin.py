from django.contrib import admin
from . models import Staff
# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'role', 'is_active', 'hire_date',
    )
    list_editable = ('is_active',)
    list_display_links = ('id', 'first_name')
    list_per_page = 25
    search_fields = ('id', 'first_name', 'role')
    list_filter = ('hire_date', 'is_active')


admin.site.register(Staff, StaffAdmin)
