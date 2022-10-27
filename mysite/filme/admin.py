from django.contrib import admin

from .models import Generos, Filmes


admin.site.register(Generos)

class FilmesAdmin(admin.ModelAdmin):
    list_display = ['filme', 'genero', 'quantidade', 'preco']
admin.site.register(Filmes, FilmesAdmin)