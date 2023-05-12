from django.shortcuts import render

from .models import Pessoa


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas": pessoas})


# Create your views here.
def salvar(request):
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome)
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas": pessoas})


def editar(resquest):
    pass
