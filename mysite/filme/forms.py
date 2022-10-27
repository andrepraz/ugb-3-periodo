from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Filmes

class FilmeForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['filme', 'genero', 'quantidade', 'preco']
        #fields = '__all__'