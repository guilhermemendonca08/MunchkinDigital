from Imports.Cartas.carta_classe import Classe


class Ladrao(Classe):
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

    def Backstabbing(self):
        pass

    def Theft(self):
        pass

