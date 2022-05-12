from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    nr_reservas = models.IntegerField()
    contrato = models.BooleanField()
    
    def __str__(self):
        return self.nome