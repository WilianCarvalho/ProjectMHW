from django.db import models

#Classe Registro de Cliente
class RegistroCliente(models.Model):

    NumCnpj = models.CharField(max_length=14)
    RazSoci = models.CharField(max_length=255)
    NomFant = models.CharField(max_length=255)
    DataGer = models.DateTimeField(auto_now_add=True)
    DataAut = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.RazSoci

#Classe Registro de Contato
class RegistroContato(models.Model):

    TipoContato = (
        ('TEL', 'Telefone'),
        ('WAP', 'WhatsApp'),
        ('EML', 'E-mail'),
    )

    Situacao = (
        ('PRP','Prospecção'),
        ('ART','Aguardando Retorno'),
        ('PEF','Pedido Efetivado'),
        ('CAN','Cancelamento'),
        ('SIT','Sem Interresse'),
        ('PCA','Pedido Cancelado'),
        ('COB','Cobrança')
    )

    NumCnpj = models.CharField(max_length=14)
    DataCon = models.DateField(auto_now_add=True)
    HoraCon = models.TimeField(auto_now_add=True)
    TipoCon = models.CharField(
        max_length = 3,
        choices = TipoContato,
    )
    SitiCon = models.CharField(
        max_length = 3,
        choices = Situacao,
    ) 
    ObseCon = models.TextField()
    
    def __str__(self):
        return self.NumCnpj