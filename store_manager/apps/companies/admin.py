from django.contrib import admin #antes de cadastrar tem q ter algumas empresas ja. ai eu vi que essa funcionalidade admin.py simula um banco de dados.
from .models import Empresa, Filial

admin.site.register(Empresa)
admin.site.register(Filial)