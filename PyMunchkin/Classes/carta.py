from PPlay.gameimage import GameImage


class Carta:
    def __init__(self, imagepath, nome, descricao, efeito, tipo, deckOrigem=None):
        self.imagem = GameImage(imagepath)
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.tipo = tipo  # item, monstro, maldicao, etc
        self.deckOrigem = deckOrigem  # tesouro/dungeon

    def debug(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Efeito: {self.efeito}")
        print(f"Tipo: {self.tipo}")
        print(f"Deck de origem: {self.deckOrigem}")

    def jogarCarta(self, alvo):
        pass

    def executarEfeito(self, alvo):
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

    def get_deckOrigem(self):
        return self.deckOrigem

    def get_acceptable_targets(self):
        return []
