from django.db import models

# Create your models here.

class tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    prazo = models.DateField()

    def __str__(self) -> str:
        return self.nome