from Classes.carta_classe import Classe


class Guerreiro(Classe):
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

    def Berserking(self):
        pass

