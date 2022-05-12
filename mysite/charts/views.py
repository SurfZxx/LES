from django.shortcuts import render
from models import Clientes
from models import Reservas


# Create your views here.
def index(request):
    return render(request, 'index.html')




    
def clientesView(request):
    contrato_number = Clientes.objects.filter(contrato='1').count()
    contrato_number = int(contrato_number)
    
    
    sem_contrato_number = Clientes.objects.filter(contrato='0').count()
    sem_contrato_number = int(sem_contrato_number)
    
