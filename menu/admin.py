from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class AdminMenu(admin.ModelAdmin):
    list_display = ('title', 'name', 'parent', 'url')
    list_filter = ('name', )
