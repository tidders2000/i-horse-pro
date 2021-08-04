from django.contrib import admin


from .models import Profile,Register_email
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Register_email)


# Register your models here.
