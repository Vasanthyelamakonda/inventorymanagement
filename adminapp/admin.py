from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin
from .models import Brand

@admin.register(Brand)
class Brand_resources(ImportExportModelAdmin):
    class Meta:
        model=Brand

