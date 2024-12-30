from Classes.carta_classe import Classe


class Ladrao(Classe):
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

    def Backstabbing(self):
        pass

    def Theft(self):
        pass

