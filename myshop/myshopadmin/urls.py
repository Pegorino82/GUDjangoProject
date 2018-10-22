from django.urls import path, re_path

from myshopadmin.views import ModelCreateProduct, ModelUpdateProduct, ModelDeleteProduct, ModelDetailProduct, \
    ModelListProduct, index

app_name = 'myshopadminapp'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<app>\w+)/(?P<model>\w+)/create/$', ModelCreateProduct.as_view(), name='create'),
    re_path(r'^(?P<app>\w+)/(?P<model>\w+)/update/(?P<pk>\d+)/$', ModelUpdateProduct.as_view(), name='update'),
    re_path(r'^(?P<app>\w+)/(?P<model>\w+)/delete/(?P<pk>\d+)/$', ModelDeleteProduct.as_view(), name='delete'),
    re_path(r'^(?P<app>\w+)/(?P<model>\w+)/(?P<pk>\d+)/$', ModelDetailProduct.as_view(), name='detail'),
    re_path(r'^(?P<app>\w+)/(?P<model>\w+)/$', ModelListProduct.as_view(), name='list'),
]
