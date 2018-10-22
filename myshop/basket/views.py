from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from basket.models import Basket
from products.models import Product


def basket(request):
    template_name = 'basket/basket.html'

    bascket = Basket.objects.filter(user=request.user)

    return render(request, template_name, {'basket': bascket})

def add_product(request, **kwargs):
    pk = kwargs.get('pk')
    prod = Product.objects.get(pk=pk)

    old_basket = Basket.objects.filter(product=prod, user=request.user)
    if old_basket:
        old_basket[0].quantity += 1
        old_basket[0].save()
    else:
        new_basket = Basket(product=prod, user=request.user)
        new_basket.quantity += 1
        new_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_product(request, **kwargs):
    pk = kwargs.get('pk')
    prod = Product.objects.get(pk=pk)

    old_basket = Basket.objects.filter(product=prod, user=request.user)
    if old_basket:
        old_basket[0].quantity -= 1
        old_basket[0].save()
    else:
        new_basket = Basket(product=prod, user=request.user)
        new_basket.quantity -= 1
        new_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
