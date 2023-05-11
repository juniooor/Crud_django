from django.urls import path

from .views import home, salvar, editar

urlpatterns = [
    path('',home),
    path('salvar/', salvar, name="salvar")
    path('editar/<int:id>', editar, name="editar")
]

