from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Product, Category
from products.forms import ProductModelForm


def catalog(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'limit_products': Product.get_limit(5)
    }

    return render(request, 'products/catalog.html', context)


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


class ModelCreateProduct(CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('productsapp:list')


class ModelListProduct(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'results'


class ModelDetailProduct(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class ModelUpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('productsapp:catalog')


class ModelDeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('productsapp:catalog')
