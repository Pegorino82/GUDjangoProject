from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Product, Category
from products.forms import ProductModelForm


def catalog(request):

    categories = Category.objects.all()
    categories_paginator = Paginator(categories, 4)
    categories_page = request.GET.get('page')
    categories_items = categories_paginator.get_page(categories_page)
    context = {
        'categories': categories_items,
        'all_categories': Category.objects.all(),
        'limit_products': Product.get_limit(2)
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ModelListProduct, self).get_context_data(**kwargs)
        context['results'] = self.items
        return context

    def get(self, request, *args, **kwargs):
        query = self.model.objects.all()
        paginator = Paginator(query, 2)
        page = request.GET.get('page')
        self.items = paginator.get_page(page)
        return super(ModelListProduct, self).get(request, *args, **kwargs)


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
