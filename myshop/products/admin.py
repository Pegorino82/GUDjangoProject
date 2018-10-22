from django.contrib import admin

# Register your models here.

from products import models

admin.site.register(models.Category)
admin.site.register(models.ProductMarker)
admin.site.register(models.Product)
