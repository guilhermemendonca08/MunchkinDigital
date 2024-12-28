from random import randint
from PPlay.gameimage import GameImage


class CardStack:
    def __init__(self, imagepath):
        self.imagem = GameImage(imagepath)
        self.pilha = []

    # PPLAY stuff
    def draw(self):
        self.imagem.draw()

    def set_position(self, x, y):
        self.imagem.set_position(x, y)

    # End of PPLAY stuff

    def getSize(self):
        return len(self.pilha)

    def isEmpty(self):
        return not self.pilha

    def peek(self):
        if self.isEmpty():
            return None
        return self.pilha[-1]

    def push(self, value):
        self.pilha.append(value)

    def push_bottom(self, value):
        self.pilha.insert(0, value)

    def push_wherever(self, value):
        if self.isEmpty():
            self.pilha.append(value)
            return
        self.pilha.insert(randint(0, self.getSize() - 1), value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.pilha.pop()

    def shuffle(self):
        nova_pilha = []
        tamanho = self.getSize()
        for i in range(tamanho):
            random_index = randint(0, tamanho - 1)
            nova_pilha.append(self.pilha.pop(random_index))
            tamanho -= 1
        self.pilha = nova_pilha

