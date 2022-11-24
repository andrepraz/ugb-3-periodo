from django.forms import ModelForm, TextInput, Select
from .models import NotasEntradas

class NotasEntradasForm(ModelForm):
    class Meta:
        model = NotasEntradas
        #fields = '__all__'
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': Select(attrs={'class': 'select'}),
            'quantidade': TextInput(attrs={'class': 'input'}),
            'preco': TextInput(attrs={'class': 'input'}),
        }