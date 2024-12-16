from django.contrib import admin
from .models import *

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug')
    search_fields = ('title', 'content')
    list_filter = ('author',)
    row_id_fields = ['author',]
    