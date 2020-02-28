from django.shortcuts import render
from sys import path
from core.arquivos import *
from datetime import date


def main_dash(request):
    path.append('C:/Users/carlo/PycharmProjects/fc)')
    anoatual = date.today().year
    mesatual = date.today().month
    anotrabalho = anoatual
    mestrabalho = mesatual

    arqlistameiossaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'MeiosSaldo')
    listameiossaldo = arqlistameiossaldo.ler()

    arqlistameios = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeios.pck1', 'Meios')
    listameios = arqlistameios.ler()

    lista_saldo = []
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            nomemeio = list(filter(lambda meio: meio["cod"] == x["cod"], listameios))[0]["nome"]
            registro = x
            registro['nomemeio'] = nomemeio
            lista_saldo.append(registro.copy())
    return render(request, 'core/maindash.html', {'listasaldo': lista_saldo})
