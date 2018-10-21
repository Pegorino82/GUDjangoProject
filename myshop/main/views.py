from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from main.models import MainPageContent, Author
from main.forms import MainAuthorForm, MainArticleModelForm, MainAuthorModelForm


def index(request):  # list_articles
    template_name = 'main/index.html'
    context = {
        'results': MainPageContent.objects.all()
    }

    return render(request, template_name, context)


###################forms.Form################################
# def create_author(request):
#     template_name = 'main/create_author.html'
#     success_url = reverse_lazy('mainapp:list_author')
#     form = MainAuthorForm(request.POST)
#
#     upl_img = request.FILES.get('photo')
#
#     if request.method == 'POST':
#
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             lastname = form.cleaned_data.get('lastname')
#             photo = upl_img
#
#             Author.objects.create(
#                 name=name,
#                 lastname=lastname,
#                 photo=photo
#             )
#
#             return redirect(success_url)
#     return render(request, template_name, {'form': form})
#
#
# def update_author(request, **kwargs):
#     template_name = 'main/update_author.html'
#     success_url = reverse_lazy('mainapp:list_author')
#     pk = kwargs.get('pk')
#     obj = Author.objects.get(pk=pk)
#     # TODO как заполнить поля формы полями выбранного объекта?
#     form = MainAuthorForm()
#     form.name = obj.name
#     form.lastname = obj.lastname
#     form.photo = obj.photo
#
#     if request.method == 'POST':
#         form = MainAuthorForm(
#             request.POST
#         )
#
#         if form.is_valid:
#             form.save()
#
#             return redirect(success_url)
#     return render(request, template_name, {'form': form, 'obj': obj})
###################forms.Form################################

def create_author(request):
    template_name = 'main/create_author.html'
    success_url = reverse_lazy('mainapp:list_author')
    form = MainAuthorModelForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect(success_url)

    return render(request, template_name, {'form': form})


def update_author(request, **kwargs):
    template_name = 'main/update_author.html'
    success_url = reverse_lazy('mainapp:list_author')
    pk = kwargs.get('pk')
    obj = Author.objects.get(pk=pk)
    form = MainAuthorModelForm(instance=obj)

    if request.method == 'POST':
        form = MainAuthorModelForm(
            request.POST,
            request.FILES,
            instance=obj
        )
        if form.is_valid:
            form.save()
            return redirect(success_url)

    return render(request, template_name, {'form': form})


def detail_author(request, **kwargs):
    template_name = 'main/detail_author.html'
    pk = kwargs.get('pk')
    obj = Author.objects.get(pk=pk)

    return render(request, template_name, {'object': obj})


def delete_author(request, **kwargs):
    template_name = 'main/delete_author.html'
    success_url = reverse_lazy('mainapp:list_author')
    pk = kwargs.get('pk')
    obj = Author.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect(success_url)

    return render(request, template_name, {'object': obj})


def list_author(request):
    template_name = 'main/list_author.html'
    context = {
        'results': Author.objects.all()
    }

    return render(request, template_name, context)


def create_article(request):
    template_name = 'main/create_article.html'
    success_url = reverse_lazy('mainapp:index')
    form = MainArticleModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, template_name, {'form': form})


def update_article(request, **kwargs):
    template_name = 'main/update_article.html'
    success_url = reverse_lazy('mainapp:index')
    pk = kwargs.get('pk')
    obj = MainPageContent.objects.get(pk=pk)

    # TODO надо передать в форму время из модели
    form = MainArticleModelForm(instance=obj)

    if request.method == 'POST':
        form = MainArticleModelForm(
            request.POST,
            instance=obj
        )
        if form.is_valid:
            form.save()
            return redirect(success_url)

    return render(request, template_name, {'form': form})


def detail_article(request, **kwargs):
    template_name = 'main/detail_article.html'
    pk = kwargs.get('pk')
    obj = MainPageContent.objects.get(pk=pk)

    return render(request, template_name, {'object': obj})


def delete_article(request, **kwargs):
    template_name = 'main/delete_article.html'
    success_url = reverse_lazy('mainapp:index')
    pk = kwargs.get('pk')
    obj = MainPageContent.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect(success_url)

    return render(request, template_name, {'object': obj})
