from django.urls import path

from .views import editar, home, salvar, update

urlpatterns = [
    path("", home),
    path("salvar/", salvar, name="salvar"),
    path("editar/<int:id>", editar, name="editar"),
    path("update/<int:id>", update, name="update"),
]
