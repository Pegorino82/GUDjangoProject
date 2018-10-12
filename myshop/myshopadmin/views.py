from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from products.models import Product

class ModelCreateProduct(CreateView):
    model = Product
    fields = []
    template_name = 'myshopadmin/create.html'
    success_url = reverse_lazy('products:catalog')


class ModelUpdateProduct(UpdateView):
    model = Product
    fields = []
    template_name = 'myshopadmin/update.html'
    success_url = reverse_lazy('products:catalog')

class ModelDeleteProduct(DeleteView):
    model = Product
    fields = []
    template_name = 'myshopadmin/delete.html'
    success_url = reverse_lazy('products:catalog')

class ModelDetailProduct(DetailView):
    model = Product
    fields = []
    template_name = 'myshopadmin/detail.html'
    success_url = reverse_lazy('products:catalog')

class ModelListProduct(ListView):
    model = Product
    fields = []
    template_name = 'myshopadmin/list.html'
    success_url = reverse_lazy('products:catalog')