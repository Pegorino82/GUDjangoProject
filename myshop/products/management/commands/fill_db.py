from django.core.management.base import BaseCommand, CommandError

from products.models import Product, Category, ProductMarker
from images.models import Image


class Command(BaseCommand):
    help = '''fills DB'''

    def add_arguments(self, parser):
        parser.add_argument('--random', action='store_const', const=101)

    def handle(self, *args, **options):

        if options['random']:

            images = Image.objects.all()
            categories = Category.objects.all()
            markers = ProductMarker.objects.all()

            import random
            products = []
            ammount = options['random']

            for i in range(1, ammount):
                products.append(
                    {
                        'name': 'Product_' + str(i),
                        'short_text': 'Product short text',
                        'long_text': 'Product long text',
                        'now_price': random.randint(1000, 1500),
                        'old_price': random.randint(1500, 2000),
                        'product_marker': random.choice(markers),
                        'category': random.choice(categories),
                        'image': random.choice(images)
                    }
                )

            for prod in products:
                try:
                    product = Product(**prod)
                    product.save()
                except Exception as err:
                    print(f'Exception: {err}')
