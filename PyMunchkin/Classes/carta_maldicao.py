from Classes.carta import Carta


class Maldicao(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        tipoMaldicao,
        duracao,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo)
        self.tipoMaldicao = tipoMaldicao
        self.duracao = duracao

