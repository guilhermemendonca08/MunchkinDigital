from Classes.carta import Carta


class Raca(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        nomeRaca,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.nomeRaca = nomeRaca

