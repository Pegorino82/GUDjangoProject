from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.http import JsonResponse

from products.models import Product, ProductMarker, Category
from images.models import Image


# ?name=Api_product&short_text=short_text&long_text=long_text&now_price=1000&old_price=5000&product_marker=1&category=32&image=3

def rest_product_create(request):
    req = request.GET

    name = req.get('name')
    short_text = req.get('short_text')
    long_text = req.get('long_text')
    now_price = req.get('now_price')
    old_price = req.get('old_price')
    product_marker = req.get('product_marker')
    category = req.get('category')
    image = req.get('image')

    product = Product.objects.create(
        name=name,
        short_text=short_text,
        long_text=long_text,
        now_price=float(now_price),
        old_price=float(old_price),
        product_marker=ProductMarker.objects.get(id=int(product_marker)),
        category=Category.objects.get(id=int(category)),
        image=Image.objects.get(id=int(image))
    )
    product.save()

    obj = get_object_or_404(Product, name=name)
    data = obj.__dict__
    data.pop('_state')
    data.pop('id')

    return JsonResponse(
        {
            'results': data
        }
    )


def rest_product_list(request):
    query_set = get_list_or_404(Product)
    data = list(
        map(
            lambda itm: {
                'name': itm.name,
                'short_text': itm.short_text[:50] + '...' if len(itm.short_text) > 50 else itm.short_text,
                'now_price': itm.now_price,
                'old_price': itm.old_price,
                'currency': itm.currency,
                'product_marker': itm.product_marker.corner,
                'category': itm.category.name,
                'image': itm.image.img.url
            },
            query_set
        )
    )

    return JsonResponse(
        {
            'results': data
        }
    )


def rest_product_detail(request, **kwargs):
    pk = kwargs.get('pk')
    obj = get_object_or_404(Product, id=pk)
    data = {
                'name': obj.name,
                'short_text': obj.short_text[:50] + '...' if len(obj.short_text) > 50 else obj.short_text,
                'long_text': obj.short_text[:50] + '...' if len(obj.long_text) > 50 else obj.long_text,
                'now_price': obj.now_price,
                'old_price': obj.old_price,
                'currency': obj.currency,
                'product_marker': obj.product_marker.corner,
                'category': obj.category.name,
                'image': obj.image.img.url
            }

    return JsonResponse(
        {
            'results': data
        }
    )


# ?name=Api_updated
def rest_product_update(request, **kwargs):
    pk = kwargs.get('pk')
    obj = get_object_or_404(Product, id=pk)
    for key, val in request.GET.items():
        setattr(obj, key, val)
    obj.save()

    data = obj.__dict__
    data.pop('_state')
    data.pop('id')

    return JsonResponse(
        {
            'results': data
        }
    )

def rest_product_delete(request, **kwargs):
    pk = kwargs.get('pk')
    obj = get_object_or_404(Product, id=pk)
    obj.delete()

    return JsonResponse(
        {
            'results': 'OK'
        }
    )