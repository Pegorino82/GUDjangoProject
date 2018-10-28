from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.http import JsonResponse

from products.models import Category


def rest_category_list(request):
    query_set = get_list_or_404(Category)
    data = [i.__dict__ for i in query_set]
    for d in data:
        d.pop('_state')
        d.pop('id')

    return JsonResponse(
        {
            'results': data
        }
    )

def rest_category_detail(request, **kwargs):
    pk = kwargs.get('pk')
    obj = get_object_or_404(Category, id=pk)
    data = obj.__dict__
    data.pop('_state')
    data.pop('id')

    return JsonResponse(
        {
            'results': data
        }
    )
