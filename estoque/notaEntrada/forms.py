from django.forms import ModelForm
from .models import NotasEntradas

class NotasEntradasForm(ModelForm):
    class Meta:
        model = NotasEntradas
        #fields = '__all__'
        fields = ['produto', 'quantidade', 'preco']