from PPlay.gameimage import GameImage


class Carta:
    def __init__(self, imagepath, nome, descricao, efeito, tipo):
        self.imagem = GameImage(imagepath)
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.tipo = tipo

    def executarEfeito(self):
        pass
    
    def get_descricao(self):
        return self.descricao

    def draw(self):
        self.imagem.draw()

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo
