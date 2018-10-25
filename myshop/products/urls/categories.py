from django.urls import path

from products.views import (
    category,
    ModelCreateCategory,
    ModelListCategoriy,
    ModelUpdateCategory,
)

app_name = 'categoriesapp'

urlpatterns = [
    path('category/<str:category>/', category, name='category'),
    path('create/', ModelCreateCategory.as_view(), name='create'),
    path('list/', ModelListCategoriy.as_view(), name='list'),
    path('update/<int:pk>/', ModelUpdateCategory.as_view(), name='update'),
]
