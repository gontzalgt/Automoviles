from django.contrib import admin
from .models import Coche
# Register your models here.

class CocheAdmin(admin.ModelAdmin):
    list_display = (
        'matr',
        'fecha',
        'marca',
        'modelo',
    )
    search_fields = ('matr'),
    list_filter = ('marca'),

admin.site.register(Coche, CocheAdmin)