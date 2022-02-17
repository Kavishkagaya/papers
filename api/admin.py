from django.contrib import admin
from .models import Subjects,Papers

# Register your models here.
#admin.site.register(Article)

@admin.register(Subjects)
class Subjectsmodel(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)

@admin.register(Papers)
class Papersmodel(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)