from random import randint


class ListaCircular:
    def __init__(self):
        self.lista = []
        self.atual = 1

    def __iter__(self):
        return iter(self.lista)

    def adiciona(self, item):
        self.lista.append(item)
        self.atual += 1

    def get_size(self):
        return len(self.lista)

    def proximo(self):
        if self.get_size() == 0:
            return None
        if self.atual >= len(self.lista) - 1:
            self.atual = 0
        else:
            self.atual += 1
        return self.lista[self.atual]

    def exporta_lista(self):
        return self.lista

    def proximo_depois_de(self, item):
        if self.get_size() == 0:
            return None
        self.atual = self.lista.index(item)
        if self.atual >= len(self.lista) - 1:
            return self.lista[0]
        else:
            return self.lista[self.atual + 1]

    def get_anterior(self):
        if self.get_size() == 0:
            return None
        if self.atual >= len(self.lista) - 1:
            self.atual = 0
        return self.lista[self.atual - 1]

    def get_atual(self):
        if self.get_size() == 0:
            return None
        if self.atual >= len(self.lista) - 1:
            self.atual = 0
        return self.lista[self.atual]

    def random_starting_point(self):
        self.atual = randint(0, self.get_size() - 1)

