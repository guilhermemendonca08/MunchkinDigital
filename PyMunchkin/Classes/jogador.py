from constants import CARD_WIDTH, CARD_HEIGHT
from PPlay.gameimage import GameImage
from Classes.personagem import Personagem
from Classes.inventario import Inventario


class Jogador:
    def __init__(self, nome, avatarImage):
        self.avatar = GameImage(avatarImage)
        self.nome = nome
        self.personagem = Personagem()
        self.mao = []
        self.inventario = Inventario()

    # Avatar stuff
    def set_position(self, x, y):
        self.avatar.set_position(x, y)

    def get_avatar_x(self):
        return self.avatar.width

    def get_avatar_y(self):
        return self.avatar.height

    def get_nome(self):
        return self.nome

    # Combate
    def calcularForcaCombate(self):
        return self.personagem.calcularForcaCombate()

    # Card Managment
    def get_card(self, card):
        self.mao.append(card)

    def remove_card(self, card):
        self.mao.remove(card)

    def receber_carta(self, carta):
        self.mao.append(carta)

    def get_size_mao(self):
        return len(self.mao)

    # Draws
    def draw(self):
        self.avatar.draw()

    def draw_mao(self, offset_x, offset_y):
        peek_window = 100
        hand_pixel_size = peek_window * (self.get_size_mao() - 1) + CARD_WIDTH
        for i, card in enumerate(self.mao):
            card.imagem.set_position(offset_x + (-hand_pixel_size/2 + i * peek_window), offset_y + 0)
            card.draw()
