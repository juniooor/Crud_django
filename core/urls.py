from django.urls import path

from .views import delete, editar, home, salvar, update

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
    path("editar/<int:id>", editar, name="editar"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
]
