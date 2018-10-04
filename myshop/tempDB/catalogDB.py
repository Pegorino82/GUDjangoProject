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
    'Category_1': {
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

ammount_in_cat = {category: len(catalog[category].keys()) for category in catalog}
page_content = {k: {p: i for p, i in list(v.items())[:5]} for k, v in catalog.items()}
for category in page_content:
    page_content[category].update({'number': ammount_in_cat[category]})

if __name__ == '__main__':

    # for k, v in catalog.items():
    #     print(k)
    #     for p, i in list(v.items())[:5]:
    #         print(i)

    # new = {k: {p: i for p, i in list(v.items())[:5]} for k, v in catalog.items()}
    #
    # for k, v in new.items():
    #     print(k)
    #     for p, i in v.items():
    #         print(p, i)

    ammount_in_cat = {category: len(catalog[category].keys()) for category in catalog}
    page_content = {k: {p: i for p, i in list(v.items())[:5]} for k, v in catalog.items()}
    for category in page_content:
        page_content[category].update({'ammount': ammount_in_cat[category]})

    for k, v in page_content.items():
        print(k)
        for i, t in v.items():
            print(i, t)