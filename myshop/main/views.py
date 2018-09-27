from django.shortcuts import render

from tempDB import indexDB


# Create your views here.


def index(request):
    context = {
        'results': indexDB.index
    }

    return render(request, 'main/index.html', context)
