from django.db import models #talvez seria bom usar um hash para a senha (nao sei como faz)

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome


class Filial(models.Model):
    nome = models.CharField(max_length=100)
    dono = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='filiais')

    def __str__(self):
        return self.nome