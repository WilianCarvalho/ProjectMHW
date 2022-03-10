from django.contrib import admin

from .models import RegistroCliente
from .models import RegistroContato

admin.site.register(RegistroCliente)
admin.site.register(RegistroContato)