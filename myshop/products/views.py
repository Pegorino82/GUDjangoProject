from django.shortcuts import render

from tempDB import catalogDB, indexDB

# Create your views here.

from django.http import HttpResponse, JsonResponse


def catalog(request):

    context = {
        'results': catalogDB.catalog
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
    context = {
        'results': catalogDB.catalog
    }

    result = {
        'category': category,
        'product': context['results'][category][pk],
        'pk': pk
    }

    return render(request,
                  'products/product.html',
                  result
                  )

