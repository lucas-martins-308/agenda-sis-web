from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
