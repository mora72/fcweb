# Funções de Abertura e Gravação de Arquivos

import pickle


def lerarqmeios():
    try:
        f = open('/Users/carlo/PycharmProjects/fc/basemeios.pck1', 'rb')
        lista = pickle.load(f)
        f.close()
    except FileNotFoundError:
        lista = []
    return lista


def gravaarqmeios(lista):
    f = open('/Users/carlo/PycharmProjects/fc/basemeios.pck1', 'wb')
    pickle.dump(lista, f)
    f.close()


def lerarqcontas():
    try:
        f = open('/Users/carlo/PycharmProjects/fc/basecontas.pck1', 'rb')
        lista = pickle.load(f)
        f.close()
    except FileNotFoundError:
        lista = []
    return lista


def gravaarqcontas(lista):
    f = open('/Users/carlo/PycharmProjects/fc/basecontas.pck1', 'wb')
    pickle.dump(lista, f)
    f.close()


def lerarqtrans():
    try:
        f = open('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'rb')
        lista = pickle.load(f)
        f.close()
    except FileNotFoundError:
        lista = []
    return lista


def gravaarqtrans(lista):
    f = open('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'wb')
    pickle.dump(lista, f)
    f.close()


def lerarqmeiossaldo():
    try:
        f = open('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'rb')
        lista = pickle.load(f)
        f.close()
    except FileNotFoundError:
        lista = []
    return lista


def gravaarqmeiossaldo(lista):
    f = open('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'wb')
    pickle.dump(lista, f)
    f.close()
