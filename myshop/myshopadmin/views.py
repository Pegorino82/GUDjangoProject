from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.apps import apps
from collections import OrderedDict

from products.models import Product


class ModelCreateProduct(CreateView):
    template_name = 'myshopadmin/create.html'
    success_url = reverse_lazy('myshopadminapp:index')

    def get(self, request, *args, **kwargs):
        app = kwargs.get('app')
        model = kwargs.get('model')
        self.model = apps.get_model(app, model.title())
        self.fields = [field.name for field in self.model._meta.__dict__.get('local_fields') if field.editable]
        return super(ModelCreateProduct, self).get(request, *args, **kwargs)


class ModelUpdateProduct(UpdateView):
    template_name = 'myshopadmin/update.html'
    success_url = reverse_lazy('myshopadminapp:index')

    def get(self, request, *args, **kwargs):
        print('*' * 100)
        print(kwargs)
        print('*' * 100)
        app = kwargs.get('app')
        model = kwargs.get('model')
        pk = kwargs.get('pk')

        self.model = apps.get_model(app, model.title())
        self.product = self.model.objects.get(pk=pk)
        self.fields = [field.name for field in self.model._meta.__dict__.get('local_fields') if field.editable]

        return super(ModelUpdateProduct, self).get(request, **kwargs)


class ModelDeleteProduct(DeleteView):
    template_name = 'myshopadmin/delete.html'
    success_url = reverse_lazy('myshopadminapp:index')

    def get(self, request, *args, **kwargs):
        print('*' * 100)
        print(kwargs)
        print('*' * 100)
        app = kwargs.get('app')
        model = kwargs.get('model')
        pk = kwargs.get('pk')

        self.model = apps.get_model(app, model.title())
        self.product = self.model.objects.get(pk=pk)
        self.fields = [field.name for field in self.model._meta.__dict__.get('local_fields') if field.editable]

        return super(ModelDeleteProduct, self).get(request, **kwargs)


class ModelDetailProduct(DetailView):
    template_name = 'myshopadmin/detail.html'
    context_object_name = 'results'

    def get(self, request, *args, **kwargs):
        print('*' * 100)
        print(kwargs)
        print('*' * 100)
        app = kwargs.get('app')
        model = kwargs.get('model')
        pk = kwargs.get('pk')

        self.model = apps.get_model(app, model.title())
        self.object = self.model.objects.get(pk=pk)
        self.fields = [field.name for field in self.model._meta.__dict__.get('local_fields') if field.editable]

        return super(ModelDetailProduct, self).get(request, **kwargs)


class ModelListProduct(ListView):
    template_name = 'myshopadmin/list.html'
    context_object_name = 'results'

    def get(self, request, *args, **kwargs):
        app = kwargs.get('app')
        model = kwargs.get('model')
        self.model = apps.get_model(app, model.title())
        self.fields = [field.name for field in self.model._meta.__dict__.get('local_fields') if field.editable]
        return super(ModelListProduct, self).get(request, *args, **kwargs)


def index(request):
    all_apps = apps.get_models()
    print('*' * 100)
    print(all_apps[-1]._meta.__dict__.keys())
    print('*' * 100)

    get_apps = {item._meta.__dict__.get('app_label') for item in all_apps}

    get_apps_dict = OrderedDict().fromkeys(sorted(get_apps))

    prep_dict = {key: [] for key in get_apps_dict}

    for item in all_apps:
        prep_dict[item._meta.__dict__.get('app_label')].append(item._meta.__dict__.get('model_name'))

    context = {'results': prep_dict}

    return render(request, 'myshopadmin/index.html', context)
