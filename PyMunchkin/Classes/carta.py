from PPlay.gameimage import GameImage


class Carta:
    def __init__(self, imagepath, nome, descricao, efeito, tipo, deckOrigem=None):
        self.imagem = GameImage(imagepath)
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.tipo = tipo  # item, monstro, maldicao, etc
        self.deckOrigem = None  # tesouro/dungeon

    def jogarCarta(self, alvo):
        # self.efeito.executarEfeito(alvo)
        pass

    def executarEfeito(self):
        pass

    def get_descricao(self):
        return self.descricao

    def draw(self):
        self.imagem.draw()

    def set_position(self, x, y):
        self.imagem.set_position(x, y)

    def scaled_draw(self, new_width, new_height):
        self.imagem.scaled_draw(new_width, new_height)

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo
