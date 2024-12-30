from Classes.carta_classe import Classe


class Mago(Classe):
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
        super().__init__(
            imagepath, nome, descricao, efeito, tipo, deckOrigem, nomeClasse
        )

    def FlightSpell(self):
        pass

    def CharmSpell(self):
        pass

