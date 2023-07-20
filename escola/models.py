from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    )

    codigo_curso = models.CharField(max_length=10)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    nivel = models.CharField(
        max_length=1, choices=NIVEL, default="B", null=False, blank=False
    )

    def __str__(self):
        return self.descricao
