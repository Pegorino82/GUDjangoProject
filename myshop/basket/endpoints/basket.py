from django.urls import path

from basket.api import rest_basket_detail, rest_basket_list

app_name = 'rest_basket'

urlpatterns = [
    path('detail/', rest_basket_detail, name='rest_detail'),
    path('list/', rest_basket_list, name='rest_list'),
]