from django.urls import path

from products.views import (
    catalog,
    product,
    ModelCreateProduct,
    ModelListProduct,
    ModelDetailProduct,
    ModelUpdateProduct,
    ModelDeleteProduct
)

app_name = 'productsapp'

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('product/<str:category>/<int:pk>/', product, name='product'),
    path('create/', ModelCreateProduct.as_view(), name='create'),
    path('list/', ModelListProduct.as_view(), name='list'),
    path('update/<int:pk>/', ModelUpdateProduct.as_view(), name='update'),
    path('detail/<int:pk>/', ModelDetailProduct.as_view(), name='detail'),
    path('delete/<int:pk>/', ModelDeleteProduct.as_view(), name='delete'),
]
