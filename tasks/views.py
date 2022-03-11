from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import RegistroCliente 


def helloWord(request):
    return HttpResponse('Hello Word')
    
def homepage(request):
    return render(request, 'tasks/homepage.html')

def registrocontatos(request, name):
    return render(request,'tasks/registrocontatos.html')

def clientlist(request):
    RegClientes = RegistroCliente.objects.all()
    return render(request, 'tasks/clientlist.html',{'RegClientes': RegClientes})

def CadCliente(request, id):
    CadCliente = get_object_or_404(RegistroCliente, pk = id)
    return render(request, 'tasks/CadClientes.html', {'CadCliente': CadCliente})
