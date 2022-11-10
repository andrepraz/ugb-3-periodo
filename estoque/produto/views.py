from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm

def listar(request):
    produtos = Produtos.objects.all()
    template_name = 'listar_produtos.html'
    context = {
        'produtos': produtos
    }
    return render(request, template_name, context)

def novo(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:listar')
    else:
        template_name = 'novo_produto.html'
        context = {
            'form': ProdutoForm(),
        }
        return render(request, template_name, context)

def alterar(request, pk):
    produto = Produtos.objects.get(id=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto:listar')
    else:
        template_name = 'alterar_produto.html'
        context = {
            'form': ProdutoForm(instance=produto),
        }
        return render(request, template_name, context)

def deletar(request, pk):
    produto = Produtos.objects.get(id=pk)
    produto.delete()
    return redirect('produto:listar')