from django.shortcuts import render, redirect
from .models import Filmes
from .forms import FilmeForm

def list_filmes(request):
    filmes = Filmes.objects.all()

    template_name = 'list_filmes.html'
    context = {
        'filmes': filmes,
        'nome': 'Estou na view list_filmes'
    }
    return render(request, template_name, context)

def new_filme(request):
    print(request.method)
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filmes_list')
    else: 
        template_name = 'new_filme.html'
        context = {
            'form': FilmeForm()
        }
    return render(request,template_name, context)

def update_filme(request, pk):
    filme = Filmes.objects.get(id=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filmes_list')
    else:
        template_name = 'update_filme.html'
        context = {
            'form': FilmeForm(instance=filme),
            'pk': pk
        }
        return render(request, template_name, context)

def delete_filme(request, pk):
    filme = Filmes.objects.get(id=pk)
    filme.delete()
    return redirect('filmes_list')