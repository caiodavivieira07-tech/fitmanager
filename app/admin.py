from django.contrib import admin
from .models import Treino

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ("nome", "objetivo", "nivel", "duracao", "criado_em")
    list_filter = ("nivel",)
    search_fields = ("nome", "objetivo")
