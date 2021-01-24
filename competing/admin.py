from django.contrib import admin
from .models import *
# Register your models here.


# class compAdmin(admin.ModelAdmin):
#     list_display = ('user', 'disipline')
#     list_filter = ('user',)
#     search_fields = ['user']


class competitonLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'disipline')
    list_filter = ('user',)
    search_fields = ['user']


admin.site.register(CompetitionLog, competitonLogAdmin)
admin.site.register(Venue)
admin.site.register(Comphorse)
