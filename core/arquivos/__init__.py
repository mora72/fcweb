# Funções de Abertura e Gravação de Arquivos
import pickle


def abrearquivo(nomelista):
    listaarqs = {'listameiosaldo': '/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1',
                 'listameios': '/Users/carlo/PycharmProjects/fc/basemeios.pck1',
                 'listacontas': '/Users/carlo/PycharmProjects/fc/basecontas.pck1',
                 'listacontasprevisto': '/Users/carlo/PycharmProjects/fc/basecontasprevisto.pck1',
                 'listacontaprovisaosaldo': '/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                 'listatrans': '/Users/carlo/PycharmProjects/fc/basetrans.pck1',
                 'listainvest': '/Users/carlo/PycharmProjects/fc/baseinvest.pck1',
                 'listaemprest': '/Users/carlo/PycharmProjects/fc/baseemprest.pck1'
                 }
    arq = Arquivolista(listaarqs[nomelista])
    return arq.ler()


def fechaarquivo(nomelista, lista):
    listaarqs = {'listameiosaldo': '/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1',
                 'listameios': '/Users/carlo/PycharmProjects/fc/basemeios.pck1',
                 'listacontas': '/Users/carlo/PycharmProjects/fc/basecontas.pck1',
                 'listacontasprevisto': '/Users/carlo/PycharmProjects/fc/basecontasprevisto.pck1',
                 'listacontaprovisaosaldo': '/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                 'listatrans': '/Users/carlo/PycharmProjects/fc/basetrans.pck1',
                 'listainvest': '/Users/carlo/PycharmProjects/fc/baseinvest.pck1',
                 'listaemprest': '/Users/carlo/PycharmProjects/fc/baseemprest.pck1'
                 }
    arq = Arquivolista(listaarqs[nomelista])
    arq.gravar(lista)


class Arquivolista:
    def __init__(self, caminho):
        self.path = caminho

    def ler(self):
        try:
            file = open(self.path, 'rb')
            listaret = pickle.load(file)
            file.close()
        except FileNotFoundError:
            listaret = []
        return listaret

    def gravar(self, lista):
        file = open(self.path, 'wb')
        pickle.dump(lista, file)
        file.close()
