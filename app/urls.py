from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("treinos/", views.lista_treinos, name="lista_treinos"),
    path("treinos/<int:id>/", views.detalhe_treino, name="detalhe_treino"),
    path("treinos/novo/", views.criar_treino, name="criar_treino"),
    path("treinos/<int:id>/editar/", views.editar_treino, name="editar_treino"),
    path("treinos/<int:id>/excluir/", views.excluir_treino, name="excluir_treino"),
    path("cadastro/", views.cadastro, name="cadastro"),
]
