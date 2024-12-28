from Classes.carta import Carta


class Monstro(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        nivel,
        qntTesouro,
        coisaRuim,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo)
        self.nivel = nivel
        self.qntTesouro = qntTesouro
        self.coisaRuim = coisaRuim
