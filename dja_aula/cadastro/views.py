from django.shortcuts import render, redirect
from .models import Inscricao
from .forms import Cadastrocriar


def home(request):
    return render(request, 'index.html')


def page(request):
    return render(request, 'cadastro.html')


def cadastro(request):
    form = Cadastrocriar(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'cadastro.html', {'form': form})


def listar(request):
    inscricao = Inscricao.objects.all()
    return render(request, 'lista.html', {'inscricao':inscricao})


def update(request, id):
    lista_cadastro = Inscricao.objects.get(id=id)
    form = Cadastrocriar(request.POST or None, instance=lista_cadastro)

    if form.is_valid():
        form.save()
        return redirect(listar)
    return render(request, 'cadastro.html', {'form': form, 'lista_cadastro': lista_cadastro})


def delete_cadastro(request, id):
    cadastrado = Inscricao.objects.get(id=id)

    if request.method == 'POST':
        cadastrado.delete()
        return redirect(listar)
    return render(request, 'delete.html', {'cadastrado': cadastrado})
