from django.shortcuts import render

from main.templates.main import catalogDB

# Create your views here.

from django.http import HttpResponse, JsonResponse


def index(request):
    with open('main/templates/main/content.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    context = {
        'results':
            [(content[itm].strip(), content[itm + 1].strip()) for itm in range(0, len(content), 2)]
    }

    # return JsonResponse(context)
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
