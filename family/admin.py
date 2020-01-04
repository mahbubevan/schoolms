from django.contrib import admin

from . models import Family
# Register your models here.


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'father_name', 'mother_name',
                    'father_phone', 'updated_at')
    list_editable = ('father_name', 'mother_name', 'father_phone')
    list_per_page = 25
    search_fields = ('father_name',)


admin.site.register(Family, FamilyAdmin)
