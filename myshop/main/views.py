from django.shortcuts import render

from tempDB import catalogDB, indexDB

# Create your views here.

from django.http import HttpResponse, JsonResponse


def index(request):
    context = {
        'results': indexDB.index
    }

    return render(request, 'main/index.html', context)


def catalog(request):

    context = {
        'results': catalogDB.catalog
    }

    return render(request, 'main/catalog.html', context)


def category(request, category):
    context = {
        'results': catalogDB.catalog
    }

    result = {
        'category': category,
        'products': context['results'][category]
    }

    return render(request,
                  'main/category.html',
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
                  'main/product.html',
                  result
                  )


# def contacts(request):
#     context = {
#         'results': [
#             'one',
#             'two',
#             'three',
#         ]
#     }
#
#     return render(request, 'main/contacts.html', context)
