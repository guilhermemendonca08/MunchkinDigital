from constants import CARD_WIDTH, CARD_HEIGHT
from PPlay.gameimage import GameImage
from Classes.personagem import Personagem


class Jogador:
    def __init__(self, nome, avatarImage):
        self.avatar = GameImage(avatarImage)
        self.nome = nome
        self.personagem = Personagem()
        self.mao = []
        self.inventario = None
        self._discard_callback = None

    # Equip stuff
    def equiparClasse(self, classe):
        if self.personagem.getClasse() is not None:
            self.discard(self.personagem.getClasse())
        self.personagem.equiparClasse(classe)

    def equiparRaca(self, raca):
        if self.personagem.getRaca() is not None:
            self.discard(self.personagem.getRaca())
        self.personagem.equiparRaca(raca)

    # Set Discard Callback.
    def set_discard_callback(self, callback):
        self._discard_callback = callback

    def discard(self, card):
        self._discard_callback(card)

    def discard_raca(self):
        self.discard(self.personagem.getRaca())
        self.personagem.equiparRaca(None)

    def discard_classe(self):
        self.discard(self.personagem.getClasse())
        self.personagem.equiparClasse(None)

    # Avatar stuff
    def get_hurtbox(self):
        return self.avatar

    def adicionaAoNivelPersonagem(self, quantidade):
        self.personagem.adicionaAoNivel(quantidade)

    def set_avatar_position(self, x, y):
        self.avatar.set_position(x, y)

    def get_avatar_x(self):
        return self.avatar.width

    def get_avatar_y(self):
        return self.avatar.height

    def get_nome(self):
        return self.nome

    # Stats
    def getNivelPersonagem(self):
        return self.personagem.getNivel()

    def getStats(self):
        stats = {}
        stats["Nome"] = self.nome
        stats["Nivel"] = self.getNivelPersonagem()
        stats["Raca"] = (
            self.personagem.getRaca().get_nome_raca()
            if (self.personagem.getRaca() is not None)
            else "Humano"
        )
        stats["Classe"] = (
            self.personagem.getClasse().get_nome_classe()
            if (self.personagem.getClasse() is not None)
            else "Nenhuma"
        )
        stats["Forca de Combate"] = self.personagem.getForcaCombate()
        return stats

    # Combate
    def calcularForcaCombate(self):
        return self.personagem.calcularForcaCombate()

    def fugir(self, monstro):
        pass

    # Card Managment
    def has_card(self, card):
        return card in self.mao

    def get_card(self, card):
        self.mao.append(card)

    def remove_card(self, card):
        self.mao.remove(card)

    def receber_carta(self, carta):
        self.mao.append(carta)

    def get_size_mao(self):
        return len(self.mao)

    # PPLAY STUFF
    # Draws
    def draw(self):
        self.avatar.draw()

    def scaled_draw(self, new_width, new_height):
        self.avatar.scaled_draw(new_width, new_height)

    def draw_mao(self, offset_x, offset_y):
        peek_window = 100
        hand_pixel_size = peek_window * (self.get_size_mao() - 1) + CARD_WIDTH
        for i, card in enumerate(self.mao):
            card.set_position(
                offset_x + (-hand_pixel_size / 2 + i * peek_window), offset_y + 0
            )
            card.draw()

    def scaled_draw_mao(self, offset_x, offset_y, new_width, new_height):
        peek_window = 60
        for i, card in enumerate(self.mao):
            card.set_position(offset_x + (i * peek_window), offset_y + 0)
            card.scaled_draw(new_width, new_height)
