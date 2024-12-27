from PPlay.gameimage import GameImage
from Classes.personagem import Personagem
from Classes.inventario import Inventario


class Jogador:
    def __init__(self, nome, mao, avatar):
        self.gimage = GameImage(avatar)
        self.nome = nome
        self.personagem = Personagem()
        self.mao = []
        self.inventario = Inventario()

    def calcularForca(self):
        return self.personagem.calcularForca()
    
    def set_position(self, x, y):
        self.gimage.set_position(x, y)

    def draw(self):
        self.gimage.draw()

