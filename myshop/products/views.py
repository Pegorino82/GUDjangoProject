from django.shortcuts import render

from .models import Category, ProductMarker, Image, Product

from tempDB import catalogDB, indexDB

# Create your views here.

from django.http import HttpResponse, JsonResponse


def catalog(request):
    context = {
        'results': catalogDB.catalog,
        'res': Product.objects.first()
    }

    return render(request, 'products/catalog.html', context)


def category(request, category):
    context = {
        'results': catalogDB.catalog
    }

    result = {
        'category': category,
        'products': context['results'][category]
    }

    return render(request,
                  'products/category.html',
                  result
                  )


def product(request, category, pk):

    result = {
        'category': category,
        'product': Product.objects.get(id=pk),
        'pk': pk
    }

    return render(request,
                  'products/product.html',
                  result
                  )
