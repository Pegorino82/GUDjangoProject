from django.shortcuts import render

from .models import MainPageContent, Author


def index(request):
    context = {
        'results': MainPageContent.objects.all()
    }

    return render(request, 'main/index.html', context)
