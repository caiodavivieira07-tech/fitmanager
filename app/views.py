from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TreinoForm
from .models import Treino


def home(request):
    treinos = Treino.objects.all()[:3]
    return render(request, "home.html", {"treinos": treinos})


def lista_treinos(request):
    treinos = Treino.objects.all().order_by("-criado_em")
    return render(request, "treinos/lista.html", {"treinos": treinos})


def detalhe_treino(request, id):
    treino = get_object_or_404(Treino, id=id)
    return render(request, "treinos/detalhe.html", {"treino": treino})


@login_required
def criar_treino(request):
    form = TreinoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_treinos")

    return render(
        request,
        "treinos/form.html",
        {"form": form, "titulo": "Novo treino"}
    )


@login_required
def editar_treino(request, id):
    treino = get_object_or_404(Treino, id=id)
    form = TreinoForm(request.POST or None, instance=treino)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("detalhe_treino", id=treino.id)

    return render(
        request,
        "treinos/form.html",
        {"form": form, "titulo": "Editar treino"}
    )


@login_required
def excluir_treino(request, id):
    treino = get_object_or_404(Treino, id=id)

    if request.method == "POST":
        treino.delete()
        return redirect("lista_treinos")

    return render(request, "treinos/excluir.html", {"treino": treino})


def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Conta criada com sucesso! Agora você pode entrar."
            )

            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "treinos/cadastro.html", {"form": form})