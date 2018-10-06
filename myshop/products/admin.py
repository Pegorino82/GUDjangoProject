from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Category)
admin.site.register(models.ProductMarker)
admin.site.register(models.Image)
admin.site.register(models.Product)
