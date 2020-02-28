# Funções de Interface
from os import system
from datetime import date


def linha(tam=42, borda=50):
    rettemp = "-" * tam
    return f'{espacos(borda)}{rettemp}'


def espacos(tam=50):
    return ' ' * tam


def bordasup(tam=10):
    for c in range(1, tam):
        print('')


def cabecalho(txt, tam=42, borda=50):
    print(f'{linha(tam, borda)}')
    print(f'{espacos(borda)}{txt.center(tam)}')
    print(f'{linha(tam, borda)}')


def menu(lista, bordae=50):
    for c, x in enumerate(lista):
        print(f'{espacos(bordae)}[ {c + 1} ] - {x}')
    print(f'{linha(42, bordae)}')
    while True:
        op = leiaint('Digite sua opção: ', bordae)
        if 1 <= op <= len(lista):
            break
        else:
            print(f'{espacos(bordae)}digite opcao valida !!!')
    return op


def main_menu():
    bordasup(3)
    print(linha(172, 0))
    print('                    [S]ETUP       [T]RANSAÇÕES       [A]NALYTICS       [P]ROVISÕES       [I]NVESTIMENTOS    '
          '   [E]MPRÉSTIMOS       [F]IM       OPÇÃO:', end='')
    op = input('').upper()
    return op


def leiaint(msg, borda=50):
    while True:
        try:
            nro = int(input(f'{espacos(borda)}{msg}'))
        except (TypeError, ValueError) as err:
            print(f'{espacos(borda)}nro invalido! {err.args}')
        else:
            return nro


def leiafloat(msg, borda=50):
    while True:
        try:
            nro = float(input(f'{espacos(borda)}{msg}'))
        except (ValueError, TypeError) as err:
            print(f'{espacos(borda)}nro invalido! {err}')
        else:
            return nro


def aguardaenter(borda=50):
    print('')
    print(f'{espacos(borda)}DIGITE ENTER PARA CONTINUAR !')
    input('')


def exibecontas(lista):
    system("cls")
    cabecalho('CONTAS DE RECEITA OU DESPESA CADASTRADOS')
    listaord = sorted(lista, key=lambda i: (i['tipo'], i['nome']))
    for x in listaord:
        print(f'{espacos(50)}{x["nome"]:<30} - {x["tipo"]}')
    aguardaenter()


def leiaconta(msg, listacontas, borda=50):
    while True:
        conta = input(f'{espacos(borda)}{msg}')
        achou = False
        for x in listacontas:
            if conta == x['nome']:
                achou = True
                break
        if achou:
            break
        else:
            print(f'{espacos(borda)}Conta não encontrada !')
            opcao = input(f'{espacos(borda)}Digite Enter para informar novamente ou 9 para ver lista de contas: ')
            if opcao == '9':
                exibecontas(listacontas)
    return conta


def e_bisexto(ano):
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                resultado = True
            else:
                resultado = False
        else:
            resultado = True
    else:
        resultado = False
    return resultado


def leiadia(msg, mes, ano, borda=50):
    while True:
        dia = leiaint(msg)
        if mes in (1, 3, 5, 7, 8, 10, 12):
            qtdedias = 31
        elif mes == 2:
            if e_bisexto(ano):
                qtdedias = 29
            else:
                qtdedias = 28
        else:
            qtdedias = 30
        if 1 <= dia <= qtdedias:
            break
        else:
            print(f'{espacos(borda)}Dia Incorreto !')
    return dia


def leiameio(msg, listameios, borda=50):
    while True:
        meio = input(f'{espacos(borda)}{msg}')
        achou = False
        for x in listameios:
            if meio == x['cod']:
                achou = True
                break
        if achou:
            break
        else:
            print(f'{espacos(borda)}Meio não encontrado !')
            opcao = input(f'{espacos(borda)}Digite Enter para informar novamente ou 9 para ver lista de meios: ')
            if opcao == '9':
                system("cls")
                cabecalho('MEIOS CADASTRADOS')
                for x in listameios:
                    print(f'{espacos(borda)}{x["cod"]} - {x["nome"]}')
                aguardaenter()
    return meio


def leiaemprestimo(msg, listaemprest,  mes, ano, borda=50):
    while True:
        emprest = input(f'{espacos(borda)}{msg}')
        achou = False
        for x in listaemprest:
            if emprest == x['nome']:
                achou = True
                break
        if achou:
            break
        else:
            print(f'{espacos(borda)}Empréstimo não encontrado !')
            opcao = input(f'{espacos(borda)}Digite Enter para informar novamente ou 9 para ver lista de empréstimos: ')
            if opcao == '9':
                exibeemprestimos(listaemprest, mes, ano)
    return emprest


def exibeemprestimos(lista, mes, ano):
    cabecalho('LISTA DE EMPRÉSTIMOS CADASTRADOS')
    listaord = sorted(lista, key=lambda i: (i['nome']))
    for x in listaord:
        if x["mes"] == mes and x["ano"] == ano:
            print(f'{espacos(50)}{x["nome"]:<30}')
    aguardaenter()
