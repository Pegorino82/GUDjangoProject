from django.contrib import admin

from customers import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'is_staff'
    ]

    list_filter = [
        'birth_date',
        'is_active',
        'last_login',
    ]

    search_fields = [
        'username',
        'first_name',
        'last_name',
    ]


admin.site.register(models.Customer, CustomerAdmin)
