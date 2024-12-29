from Classes.carta import Carta


class Amplificador(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo)

