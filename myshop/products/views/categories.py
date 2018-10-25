from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Category, Product
from products.forms import CategoryModelForm


def category(request, category):
    category_id = Category.objects.get(name=category).id

    result = {
        'category': category,
        'products': Product.objects.filter(category=category_id).order_by('-id'),
        'categories': Category.objects.all()
    }

    return render(request,
                  'products/category.html',
                  result
                  )


class ModelCreateCategory(CreateView):
    model = Category
    template_name = 'products/create.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('categoriesapp:list')


class ModelListCategoriy(ListView):
    model = Category
    template_name = 'products/list.html'
    context_object_name = 'results'


# not used
class ModelDetailCategory(DetailView):
    model = Category
    template_name = 'products/detail.html'
    context_object_name = 'results'


class ModelUpdateCategory(UpdateView):
    model = Category
    template_name = 'products/update.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('categoriesapp:list')


# not used
class ModelDeleteCategory(DeleteView):
    model = Category
    template_name = 'products/delete.html'
    success_url = reverse_lazy('categoriesapp:list')
