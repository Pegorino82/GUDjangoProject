from django.urls import path

from main import views

app_name = 'mainapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list_author/', views.list_author, name='list_author'),
    path('create_author/', views.create_author, name='create_author'),
    path('detail_author/<int:pk>/', views.detail_author, name='detail_author'),
    path('update_author/<int:pk>/', views.update_author, name='update_author'),
    path('delete_author/<int:pk>/', views.delete_author, name='delete_author'),
    path('create_article/', views.create_article, name='create_article'),
    path('update_article/<int:pk>/', views.update_article, name='update_article'),
    path('detail_article/<int:pk>/', views.detail_article, name='detail_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),

]
