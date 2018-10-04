from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class ProductMarker(models.Model):
    corner = models.CharField(
        max_length=45,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.corner


class Image(models.Model):
    '''переделать на работу с медиафайлами'''
    img = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    def __str__(self):
        if self.img:
            return self.img.split('/')[-1]


class Product(models.Model):
    name = models.CharField(max_length=150)
    short_text = models.CharField(max_length=150)
    long_text = models.CharField(max_length=350)
    now_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    product_marker = models.ForeignKey(
        'products.ProductMarker',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        'products.Image',
        on_delete=models.CASCADE
    )
