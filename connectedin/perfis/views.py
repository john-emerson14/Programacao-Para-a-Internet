from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})


def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfil.html', {'perfil': perfil, 'perfil_logado': get_perfil_logado(request),
                                           'ja_eh_contato': ja_eh_contato})


def get(perfil_id):
    if perfil_id == 1:
        return Perfil('Ely', 'ely@ifpi.edu.br', '99999-9999', 'ifpi')
    if perfil_id == 2:
        return Perfil('Pedro', 'pedro@gmail.com', '99999-8888', 'Google')
    if perfil_id == 3:
        return Perfil('Maria', 'maria@hotmail.com', '88888-7777', 'MS')


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
