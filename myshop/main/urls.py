from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('catalog/', views.catalog),
    path('contacts/', views.contacts),
]