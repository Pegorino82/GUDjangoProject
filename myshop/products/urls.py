from django.urls import path

from . import views

app_name = 'productsapp'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('product/<str:category>/<int:pk>/', views.product, name='product'),
    path('category/<str:category>/', views.category, name='category'),
]