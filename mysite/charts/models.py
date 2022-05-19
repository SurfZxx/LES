from django.db import models
import datetime

# Create your models here.
class Clientes(models.Model):
    primeiroNome = models.CharField(max_length=50)
    ultimoNome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    clientID = models.IntegerField()
    contrato = models.BooleanField()
    
    def __str__(self):
        return self.clientID
    
class Reservas(models.Model):
    reservaID = models.IntegerField()
    horaChegada = models.TimeField()
    horaSaida = models.TimeField()
    duracao = models.TimeField()
    data = models.DateField()
    clientID = Clientes.clientID
    
    
