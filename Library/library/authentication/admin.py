from django.contrib import admin
from .models import CustomUser


class UserAccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, UserAccountAdmin)

