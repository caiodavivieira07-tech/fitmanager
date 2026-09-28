from django import forms
from .models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ["nome", "objetivo", "duracao", "nivel", "descricao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "objetivo": forms.TextInput(attrs={"class": "form-control"}),
            "duracao": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "nivel": forms.Select(attrs={"class": "form-select"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
