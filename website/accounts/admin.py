from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as userA
from .forms import UserChangeForm, UserCreateForm
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(userA):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('username', 'email', 'phone')
    list_filter = ('username', 'is_active')

    fieldsets = (
        ('user', {'fields': ('username', 'email')}),
        ('Personal info', {'fields': ('is_admin', )}),
        ('Permissions', {'fields': ('is_active', )}),
    )

    add_fieldsets = (
        (None, {'fields' : ('username', 'email', 'phone', 'pass_1', 'pass_2')})
    )

    search_fields = ('username', )

    ordering = ('username', )

    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)



