from django.contrib import admin
from .models import *
# Register your models here.


class yardAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Client, yardAdmin)
admin.site.register(Staff, yardAdmin)
