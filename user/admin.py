from django.contrib import admin
from .models import Account, UserToken

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


admin.site.register(Account, AccountAdmin)
admin.site.register(UserToken)