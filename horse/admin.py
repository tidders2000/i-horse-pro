from django.contrib import admin

# Register your models here.
from .models import Horse


class HorseAdmin(admin.ModelAdmin):
    list_display = ('user', 'showName')
    list_filter = ('user',)
    search_fields = ['user']


admin.site.register(Horse, HorseAdmin)
