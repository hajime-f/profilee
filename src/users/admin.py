from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


# @admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'last_name_kana', 'first_name_kana',
         'email', 'sex', 'birthday', 'postal_code', 'prefecture', 'address', 'building', 'tel',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('get_full_name', 'get_full_name_kana', 'email', 'sex', 'birthday',
                    'postal_code', 'prefecture', 'address', 'building', 'tel', 'is_staff',)
    search_fields = ('email',)
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User)
