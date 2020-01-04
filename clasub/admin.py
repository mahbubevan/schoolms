from django.contrib import admin
from . models import Clasub
# Register your models here.


class ClasubAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'teacher', 'lession_time',
                    'updated_at', 'is_active'
                    )

    list_editable = ('is_active', 'teacher')
    list_filter = ('is_active', 'subject')
    search_fields = ('id', 'subject')
    list_per_page = 25


admin.site.register(Clasub, ClasubAdmin)
