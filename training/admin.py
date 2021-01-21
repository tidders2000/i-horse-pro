from django.contrib import admin
from .models import *
# Register your models here.


class imageAdmin(admin.ModelAdmin):
    list_display = ('user', 'disipline')
    list_filter = ('user',)
    search_fields = ['user']


class trainingLog(admin.ModelAdmin):
    list_display = ('user', 'disipline')
    list_filter = ('user',)
    search_fields = ['user']


admin.site.register(CustomImages, imageAdmin)
admin.site.register(TrainingLog, trainingLog)
admin.site.register(Objectives)
