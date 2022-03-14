from django import forms

from .models import RegistroCliente

class NovoCliente(forms.ModelForm):

    class Meta:
        model = RegistroCliente
        fields = ('NumCnpj','RazSoci','NomFant')