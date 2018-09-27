from collections import OrderedDict

'''
{product_category: {
    product_id: {
        product info
                }
    }
}
'''

catalog = OrderedDict({
    'products_1': {
        1: {
            'corner': 'corner_new',
            'img': 'main/images/products/img_1.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None},
            'text': 'b'
        },
        2: {
            'corner': 'corner_hot',
            'img': 'main/images/products/img_2.jpg',
            'name': 'Product',
            'price': {'now': 750, 'old': 1000}
        },
        3: {
            'corner': None,
            'img': 'main/images/products/img_3.jpg',
            'name': 'Product',
            'price': {'now': 1500, 'old': None}
        },
        4: {
            'corner': None,
            'img': 'main/images/products/img_4.jpg',
            'name': 'Product',
            'price': {'now': 1500, 'old': None}
        },
        5: {
            'corner': None,
            'img': 'main/images/products/img_5.jpg',
            'name': 'Product',
            'price': {'now': 1500, 'old': None}
        },
        6: {
            'corner': None,
            'img': 'main/images/products/img_6.jpg',
            'name': 'Product',
            'price': {'now': 1500, 'old': None}
        }
    },
    'products_2': {
        7: {
            'corner': None,
            'img': 'main/images/products/img_1.jpg',
            'name': 'Product',
            'price': {'now': 750, 'old': 1500}
        },
        8: {
            'corner': None,
            'img': 'main/images/products/img_2.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        },
        9: {
            'corner': None,
            'img': 'main/images/products/img_3.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        }
    },
    'products_3': {
        10: {
            'corner': None,
            'img': 'main/images/products/img_4.jpg',
            'name': 'Product',
            'price': {'now': 750, 'old': 1500}
        },
        11: {
            'corner': None,
            'img': 'main/images/products/img_5.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        },
        12: {
            'corner': None,
            'img': 'main/images/products/img_6.jpg',
            'name': 'Product',
            'price': {'now': 1000, 'old': None}
        }
    }
})

if __name__ == '__main__':
    def category(category):
        context = {
            'results': catalog
        }

        result = {
            'category': category,
            'products': context['results'][category]
        }

        return result['products']

    print(category('products_1'))
