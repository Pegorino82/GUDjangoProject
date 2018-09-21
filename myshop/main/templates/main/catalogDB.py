from collections import OrderedDict

catalog = OrderedDict({
    'products 1': {
        'product_1': {
            'corner': 'new',
            'img': '/static/images/products/img_1.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        },
        'product_2': {
            'corner': 'hot',
            'img': '/static/images/products/img_2.jpg',
            'name': 'Product',
            'price': {'now': 750, 'old': 1000}
        },
        'product_3': {
            'corner': None,
            'img': '/static/images/products/img_3.jpg',
            'name': 'Product',
            'price': {'now': 1500, 'old': None}
        }
    },
    'products 2': {
        'product_1': {
            'corner': 'new',
            'img': '/static/images/products/img_1.jpg',
            'name': 'Product',
            'price': {'now': 750, 'old': 1500}
        },
        'product_2': {
            'corner': 'hot',
            'img': '/static/images/products/img_2.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        },
        'product_3': {
            'corner': None,
            'img': '/static/images/products/img_3.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        }
    }
})

if __name__ == '__main__':
    print(catalog.keys())
    # print(catalog.values())
    for val in catalog.values():
        for prod in val:
            print(prod, val[prod])
