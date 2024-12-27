from django.db import models
from datetime import date

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30 )
    co_autor = models.CharField(max_length=30, blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True ,null=True )  # Aceita nulo se necessário
    data_emprestimo = models.DateTimeField(blank=True,null=True)  # Aceita nulo
    data_devolucao = models.DateTimeField(blank=True, null=True)  # Aceita nulo e pode ser deixado em branco
    tempo_duracao = models.DateField(blank=True,null=True)  # Aceita nulo

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'
