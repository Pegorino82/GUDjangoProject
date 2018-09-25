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


def contacts(request):
    context = {
        'results': [
            'one',
            'two',
            'three',
        ]
    }

    return render(request, 'main/contacts.html', context)
