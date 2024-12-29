from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'username', 'is_active', 'date_joined')
    list_display_links = ('first_name', 'username', 'email')
    readonly_fields = ('last_joined', 'password')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Accounts, AccountAdmin)
