from django.contrib import admin

# Register your models here.
from .models import Horse, Link, Tack,Images_new,Images_P


class HorseAdmin(admin.ModelAdmin):
    list_display = ('user', 'showName')
    list_filter = ('user',)
    search_fields = ['user']


admin.site.register(Horse, HorseAdmin)
admin.site.register(Link)
admin.site.register(Tack)
admin.site.register(Images_new)
admin.site.register(Images_P)
