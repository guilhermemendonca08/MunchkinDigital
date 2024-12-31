from Classes.carta_classe import Classe


class Clerigo(Classe):
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

    def Resurrection(self):
        pass

    def Turning(self):
        pass

