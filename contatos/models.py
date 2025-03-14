from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome
