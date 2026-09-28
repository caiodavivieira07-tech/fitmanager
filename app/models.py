from django.db import models

class Treino(models.Model):
    nome = models.CharField(max_length=120)
    objetivo = models.CharField(max_length=200)
    duracao = models.PositiveIntegerField(help_text="Duração aproximada em minutos")
    nivel = models.CharField(
        max_length=30,
        choices=[
            ("Iniciante", "Iniciante"),
            ("Intermediário", "Intermediário"),
            ("Avançado", "Avançado"),
        ],
        default="Iniciante",
    )
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
