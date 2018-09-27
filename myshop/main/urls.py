from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    # path('contacts/', views.contacts, name='contacts'),
    path('product/<str:category>/<int:pk>/', views.product, name='product'),
    path('category/<str:category>/', views.category, name='category'),
]