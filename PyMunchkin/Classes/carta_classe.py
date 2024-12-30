from Classes.carta import Carta


class Classe(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        nomeClasse,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.nomeClasse = nomeClasse


