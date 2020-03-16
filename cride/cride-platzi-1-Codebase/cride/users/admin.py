from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cride.users.models import User, Profile



class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')

admin.site.register(User, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'reputation', 'buy_sum')
    search_fields=('user___username', 'user__email', 'user_first_name', 'user__last_name')
    last_filter = ('reputation')