from Classes.carta import Carta


class Monstro(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        nivel,
        qntTesouro,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.nivel = nivel
        self.qntTesouro = qntTesouro
