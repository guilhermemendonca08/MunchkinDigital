from Classes.carta_classe import Classe


class Mago(Classe):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
        nome_classe,
    ):
        super().__init__(
            imagepath, nome, descricao, efeito, tipo, deck_origem, nome_classe
        )

    def FlightSpell(self):
        pass

    def CharmSpell(self):
        pass

