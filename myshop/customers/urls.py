from django.urls import path

from customers import views

app_name = 'customersapp'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    # path('product/<str:category>/<int:pk>/', views.product, name='product'),
    # path('category/<str:category>/', views.category, name='category'),
]