import random

product_markers = ['corner_hot', 'corner_new', None]
categories = ['Category_' + str(i) for i in range(1, 15)]
images = ['products/images/products/img_{}.jpg'.format(i) for i in range(1, 7)]

print(categories)

products = []

for i in range(1, 100):
    products.append(
        {
            'name': 'Product_' + str(i),
            'short_text': 'Product short text',
            'long_text': 'Product long text',
            'now_price': random.randint(1000, 1500),
            'old_price': random.randint(1500, 2000),
            'product_marker': random.choice(product_markers),
            'category': random.choice(categories),
            'image': random.choice(images)
        }
    )

for product in products:
    print(product)