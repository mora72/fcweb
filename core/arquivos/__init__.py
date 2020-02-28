# Funções de Abertura e Gravação de Arquivos
import pickle


class Arquivolista:
    def __init__(self, caminho, nome):
        self.path = caminho
        self.name = nome

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
