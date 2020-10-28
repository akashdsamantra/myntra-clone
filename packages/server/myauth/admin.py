from django.contrib import admin
from .models import User, OTP

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(OTP)
