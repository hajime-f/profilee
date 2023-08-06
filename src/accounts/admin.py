from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'last_name_kana', 'first_name_kana', 'old_last_name',
         'old_last_name_kana',  'sex', 'birthday', 'postal_code', 'prefecture', 'address', 'building', 'tel', 'url', 'photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )
    list_display = ('email', 'get_full_name', 'get_full_name_kana', 'sex', 'birthday',
                    'postal_code', 'prefecture', 'address', 'building', 'tel', 'is_staff',)
    search_fields = ('email',)
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)
    exclude = ('username',)


# # Register your models here.
# class MyUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = '__all__'


# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email',)


# class MyUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Permissions'), {
#          'fields': ('is_active', 'is_staff', 'is_superuser',)}),
#         (_('Important dates'), {
#          'fields': ('last_login', 'created_at', 'updated_at')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')
#         })
#     )
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     list_display = ('email', 'is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'is_active',)
#     search_fields = ('email',)
#     ordering = ('email',)


# admin.site.register(User, MyUserAdmin)
