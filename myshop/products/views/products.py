from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Product, Category
from products.forms import ProductModelForm


def catalog(request):
    categories = Category.objects.all()
    categories_paginator = Paginator(categories, 3)
    categories_page = request.GET.get('page')
    categories_items = categories_paginator.get_page(categories_page)
    context = {
        'categories': categories_items,
        'all_categories': Category.objects.all(),
        'limit_products': Product.get_limit(3)
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


class ModelCreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('productsapp:list')
    login_url = reverse_lazy('customersapp:customer')


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
        paginator = Paginator(query, 3)
        page = request.GET.get('page')
        self.items = paginator.get_page(page)
        return super(ModelListProduct, self).get(request, *args, **kwargs)


class ModelDetailProduct(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class ModelUpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/update.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('productsapp:catalog')
    login_url = reverse_lazy('customersapp:customer')


class ModelDeleteProduct(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('productsapp:catalog')
    login_url = reverse_lazy('customersapp:customer')

    def test_func(self):
        print('*' * 100)
        print(self.request.user.is_staff)
        return self.request.user.is_staff
