from Classes.carta import Carta


class Maldicao(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        duracao,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.duracao = duracao

