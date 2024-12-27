from Classes.carta import Carta


class Item(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        poder,
        tamanho,
        valor,
        restricao,
        usoUnico,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo)
        self.poder = poder
        self.tamanho = tamanho
        self.valor = valor
        self.restricao = restricao
        self.usoUnico = usoUnico

