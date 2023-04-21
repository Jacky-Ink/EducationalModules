from django.contrib import admin

from .models import EducationalModules

class EduModulesAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'description',)
    list_editable = ('name', 'description',)
    search_fields = ('description',)

admin.site.register(EducationalModules)
