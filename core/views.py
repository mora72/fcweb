from django.shortcuts import render, redirect
from core.arquivos import *
from datetime import date
from .forms import TransFormEdit


def main_dash(request):
    anotrabalho = date.today().year
    mestrabalho = date.today().month

    listameiossaldo = abrearquivo('listameiosaldo')
    listameios = abrearquivo('listameios')
    listacontasprevisto = abrearquivo('listacontasprevisto')
    listacontas = abrearquivo('listacontas')
    listatrans = abrearquivo('listatrans')
    listainvest = abrearquivo('listainvest')
    listacontaprovisaosaldo = abrearquivo('listacontaprovisaosaldo')

    # SALDO DE MEIOS DE PAGAMENTO
    lista_saldo = []
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            nomemeio = list(filter(lambda meio: meio["cod"] == x["cod"], listameios))[0]["nome"]
            registro = x.copy()
            registro['nomemeio'] = nomemeio
            lista_saldo.append(registro.copy())

    # RESULTADO DO MÊS
    vlr_rec_prev = vlr_des_prev = 0
    for x in listacontasprevisto:
        if mestrabalho == x['mes'] and anotrabalho == x['ano']:
            tipoconta = list(filter(lambda conta: conta["nome"] == x['nome'], listacontas))[0]["tipo"]
            if tipoconta == 'R':
                vlr_rec_prev += x['valorprevisto']
            elif tipoconta in ('D', 'E'):
                vlr_des_prev += x['valorprevisto']

    vlr_rec_real = vlr_des_real = 0
    for x in listatrans:
        if mestrabalho == x['mes'] and anotrabalho == x['ano']:
            tipoconta = list(filter(lambda conta: conta["nome"] == x['conta'], listacontas))[0]["tipo"]
            if tipoconta == 'R':
                vlr_rec_real += x['valor']
            elif tipoconta in ('D', 'E'):
                vlr_des_real += x['valor']
    vlr_rec_delta = vlr_rec_real - vlr_rec_prev
    vlr_des_delta = vlr_des_real - vlr_des_prev
    vlr_real_delta = vlr_rec_real + vlr_des_real
    vlr_prev_delta = vlr_rec_prev + vlr_des_prev
    vlr_delta_delta = vlr_rec_delta + vlr_des_delta

    listaresultmes = {'vlrrecreal': vlr_rec_real, 'vlrrecprev': vlr_rec_prev, 'vlrrecdelta': vlr_rec_delta,
                      'vlrdesreal': vlr_des_real, 'vlrdesprev': vlr_des_prev, 'vlrdesdelta': vlr_des_delta,
                      'vlrrealdelta': vlr_real_delta, 'vlrprevdelta': vlr_prev_delta, 'vlrdeltadelta': vlr_delta_delta}

    # RESULTADO PATRIMONIAL
    tot_saldo_ini = tot_saldo_fim = 0
    tot_aposent_ini = tot_aposent_fim = 0
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            tipomeio = list(filter(lambda meio: meio['cod'] == x['cod'], listameios))[0]['tipo']
            if tipomeio in ('CC', 'DI', 'CO'):
                tot_saldo_ini += x['saldo']
                tot_saldo_fim += x['saldofim']
                if tipomeio == 'CO':
                    tot_aposent_ini += x['saldo']
                    tot_aposent_fim += x['saldofim']

    for x in listainvest:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            tot_saldo_ini += x['vlrtotini']
            tot_saldo_fim += x['vlrtotfim']
            if x['tipoinvest'] != 'Fundo Provisão':
                tot_aposent_ini += x['vlrtotini']
                tot_aposent_fim += x['vlrtotfim']

    saldoprovini = saldoprovfim = 0
    for x in listacontaprovisaosaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            saldoprovini += x["saldoini"]
            saldoprovfim += x["saldofim"]
    saldo_capgiro_ini = tot_saldo_ini - saldoprovini - tot_aposent_ini
    saldo_capgiro_fim = tot_saldo_fim - saldoprovfim - tot_aposent_fim

    listapatr = {
        'saldoprovini': saldoprovini, 'saldoprovfim': saldoprovfim,
        'saldocapgiroini': saldo_capgiro_ini, 'saldocapgirofim': saldo_capgiro_fim,
        'totaposentini': tot_aposent_ini, 'totaposentfim': tot_aposent_fim,
        'totsaldoini': tot_saldo_ini, 'totsaldofim': tot_saldo_fim
    }

    return render(request, 'core/maindash.html', {'listasaldo': lista_saldo, 'listaresultmes': listaresultmes,
                                                  'listapatr': listapatr})


def trans_list(request):
    ano = date.today().year
    mes = date.today().month
    saldo = 0

    listameiossaldo = abrearquivo('listameiosaldo')
    listameios = abrearquivo('listameios')
    listatrans = abrearquivo('listatrans')

    # searchgrupo = request.GET.get('searchgrupo')  # usa o name="search" informado no input do grupos.html
    filtermeio = request.GET.get('filtermeio')
    # if type(filtermeio) is str:
    #    filtermeio = int(filtermeio)
    # if searchgrupo:
    #     lista_grupos = lista_grupos.filter(nome__icontains=searchgrupo).order_by('nome')
    listatransfiltro = []
    filternomemeioatual = ''
    if (not filtermeio) or filtermeio == '*':
        for x in listatrans:
            if x['ano'] == ano and x['mes'] == mes:
                x['nomemeio'] = list(filter(lambda meio: meio["cod"] == x["meio"], listameios))[0]["nome"]
                listatransfiltro.append(x)
    else:
        listatransfiltro = []
        saldo = ler_saldo_fim_meio(listameiossaldo, filtermeio, mes, ano)
        filternomemeioatual = list(filter(lambda meio: meio["cod"] == filtermeio, listameios))[0]["nome"]
        for x in listatrans:
            if x['meio'] == filtermeio and x['ano'] == ano and x['mes'] == mes:
                x['nomemeio'] = filternomemeioatual
                listatransfiltro.append(x)
    listatransfiltrosort = sorted(listatransfiltro, key=lambda i: i['dia'], reverse=True)
    return render(request, 'core/trans.html', {'listatransfiltro': listatransfiltrosort, 'listameios': listameios,
                                               'filtermeioatual': filtermeio,
                                               'filternomemeioatual': filternomemeioatual, 'saldo': saldo})


def trans_new(request, meio):
    ano = date.today().year
    mes = date.today().month

    if request.method == 'POST':
        form = TransFormEdit(request.POST)
        if form.is_valid():
            listatrans = abrearquivo('listatrans')
            listameiossaldo = abrearquivo('listameiosaldo')
            saldo = ler_saldo_fim_meio(listameiossaldo, form['trans_meio'].value(), mes, ano)
            saldo += float(form['trans_valor'].value())
            grava_saldo_fim_meio(listameiossaldo, form['trans_meio'].value(), mes, ano, saldo)
            registrotrans = {'ano': ano,
                             'mes': mes,
                             'dia': int(form['trans_dia'].value()),
                             'valor': float(form['trans_valor'].value()),
                             'conta': form['trans_conta'].value(),
                             'descr': form['trans_descr'].value(),
                             'meio': form['trans_meio'].value(),
                             'nomeemprest': form['trans_emprest'].value()}
            listatrans.append(registrotrans.copy())
            fechaarquivo('listatrans', listatrans)
            fechaarquivo('listameiosaldo', listameiossaldo)
            return redirect(f'/trans/?filtermeio={registrotrans["meio"]}')
        else:
            return render(request, 'core/transnew.html', {'form': form})
    else:
        form = TransFormEdit(initial={'trans_meio': meio})
        return render(request, 'core/transnew.html', {'form': form})


def ler_saldo_fim_meio(listameiossaldo, meio, mes, ano):
    saldofim = 0
    for x in listameiossaldo:
        if x["mes"] == mes and x["ano"] == ano and x['cod'] == meio:
            saldofim = x["saldofim"]
    return saldofim


def grava_saldo_fim_meio(listameiossaldo, meio, mes, ano, saldofim):
    for x in listameiossaldo:
        if x["mes"] == mes and x["ano"] == ano and x['cod'] == meio:
            x["saldofim"] = saldofim
            break
