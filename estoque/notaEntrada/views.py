from django.shortcuts import render, redirect
from .models import NotasEntradas
from .forms import NotasEntradasForm

def notaEntradaList(request):
    nota_entrada = NotasEntradas.objects.all()
    template_name = 'notaEntradaList.html'
    context = {
        'nota_entrada': nota_entrada
    }
    return render(request, template_name, context)

def notaEntradaNew(request):
    if request.method == 'POST':
        form = NotasEntradasForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + form.cleaned_data['quantidade']
            form.changed_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('entrada:notaEntradaList')
    else:
        form = NotasEntradasForm()
        template_name = 'notaEntradaNew.html'
        context = {
            'form': form,
        }
        return render(request, template_name, context)

def notaEntradaUpdate(request, pk):
    entrada = NotasEntradas.objects.get(id=pk)
    quantidade_nota_antiga = entrada.quantidade
    if request.method == 'POST':
        form = NotasEntradasForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - quantidade_nota_antiga + form.cleaned_data['quantidade']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('entrada:notaEntradaList')
    else:
        template_name = 'notaEntradaUpdate.html'
        context = {
            'form': NotasEntradasForm(instance=entrada),
            'pk': pk
        }
        return render(request, template_name, context)

def notaEntradaDelete(request, pk):
    entrada = NotasEntradas.objects.get(id=pk)
    quantidade_nota_antiga = entrada.quantidade
    entrada.produto.quantidade = entrada.produto.quantidade - quantidade_nota_antiga
    entrada.produto.save()
    entrada.delete()
    return redirect('entrada:notaEntradaList')