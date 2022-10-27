from django.contrib import admin
from django.urls import path
from core.views import index, nome
from filme.views import list_filmes, new_filme, update_filme, delete_filme

urlpatterns = [
    path('', index, name='index'),
    path('nome/', nome),
    path('filmes/', list_filmes, name='filmes_list'),
    path('new_filme/', new_filme, name='new_filme'),
    path('update_filme/<int:pk>/', update_filme, name='update_filme'),
    path('delete_filme/<int:pk>/', delete_filme, name='delete_filme'),
    path('admin/', admin.site.urls),
]
