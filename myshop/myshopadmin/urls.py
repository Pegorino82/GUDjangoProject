from django.urls import path

from myshopadmin.views import ModelCreateProduct, ModelUpdateProduct, ModelDeleteProduct, ModelDetailProduct, \
    ModelListProduct

app_name = 'myshopadminapp'

urlpatterns = [
    path('create/', ModelCreateProduct.as_view(), name='create'),
    path('update/<int:pk>/', ModelUpdateProduct.as_view(), name='update'),
    path('delete/<int:pk>/', ModelDeleteProduct.as_view(), name='delete'),
    path('<int:pk>/', ModelDetailProduct.as_view(), name='detail'),
    path('', ModelListProduct.as_view(), name='list'),
]
