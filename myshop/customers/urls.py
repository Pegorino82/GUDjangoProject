from django.urls import path

from customers import views

app_name = 'customersapp'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('detail_customer/<int:pk>/', views.detail_customer, name='detail_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('list_customer/', views.list_customer, name='list_customer'),
]
