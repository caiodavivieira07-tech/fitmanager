
from django.contrib import admin
from .models import (
    Aluno,
    Professor,
    Treino,
    Exercicio,
    Matricula,
    RegistroTreino,
)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "telefone", "data_cadastro")
    search_fields = ("usuario__username", "telefone")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "especialidade", "email")
    search_fields = ("nome", "especialidade", "email")


@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "objetivo", "nivel", "professor")
    search_fields = ("nome", "objetivo")
    list_filter = ("nivel",)


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "grupo_muscular", "series", "repeticoes")
    search_fields = ("nome", "grupo_muscular")


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "plano", "data_inicio", "data_fim", "ativa")
    list_filter = ("plano", "ativa")


@admin.register(RegistroTreino)
class RegistroTreinoAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "treino", "data_realizacao")
    list_filter = ("data_realizacao",)