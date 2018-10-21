from django.shortcuts import render

from .models import Category, Product


def catalog(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'limit_products': Product.get_limit(5)
    }

    return render(request, 'products/catalog.html', context)


def category(request, category):
    category_id = Category.objects.get(title=category).id

    result = {
        'category': category,
        'products': Product.objects.filter(category=category_id).order_by('-id'),
        'categories': Category.objects.all()
    }

    return render(request,
                  'products/category.html',
                  result
                  )


def product(request, category, pk):
    result = {
        'category': category,
        'pk': pk,
        'product': Product.objects.get(id=pk),
        'categories': Category.objects.all()
    }

    return render(request,
                  'products/product.html',
                  result
                  )
