from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Filial, Empresa

def cadastrar_filial(request):
    if request.method == 'POST':
        # Obtendo os dados do POST
        nome_filial = request.POST.get('nome')
        dono = request.POST.get('dono')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')
        empresa_id = request.POST.get('empresa_id')  # Obtendo o ID da empresa

        # Validando os campos
        if not nome_filial or not dono or not telefone or not senha or not empresa_id:
            return HttpResponse('Por favor, preencha todos os campos.')

        # Obtendo a empresa pelo ID
        empresa = get_object_or_404(Empresa, id=empresa_id)

        # Criando e salvando a nova filial no banco de dados
        nova_filial = Filial(
            nome=nome_filial,
            dono=dono,
            telefone=telefone,
            senha=senha,
            empresa=empresa
        )
        nova_filial.save()

        return HttpResponse('Filial cadastrada com sucesso!')

    empresas = Empresa.objects.all()  # Listar todas as empresas disponíveis
    return render(request, 'cadastrar_filial.html', {'empresas': empresas})
