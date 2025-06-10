from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<str:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<str:book_id>/', views.delete_book, name='delete_book'),
]
