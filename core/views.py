from django.shortcuts import render

from .models import Pessoa


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'home.html', {"pessoas": pessoas})
# Create your views here.
