from django.urls import path

from . import views

#Paginas da Internet
urlpatterns = [
    path('helloword/', views.helloWord),
    path('',views.homepage, name='Homepage'),
    path('RegistroContatos/',views.registrocontatos, name='RegistroContatos'),
    path('ListaClientes/',views.clientlist, name='ListaClientes'),
    path('RegCliente/<int:id>', views.CadCliente, name="CadCliente"),
    path('novoRegistro/',views.novoRegistro, name="novoRegistro"),
]
