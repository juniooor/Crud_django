from django.shortcuts import redirect, render

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


def editar(resquest, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(resquest, "update.html", {"pessoa": pessoa})


def update(request, id):
    nome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.save()
    return redirect(home)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect("home")
