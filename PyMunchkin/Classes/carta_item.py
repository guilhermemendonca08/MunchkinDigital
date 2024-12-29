from Classes.carta import Carta


class Item(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        poder,
        tamanho,
        valor,
        restricao,
        usoUnico,
        slot,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.poder = poder
        self.tamanho = tamanho
        self.valor = valor
        self.restricao = restricao
        self.usoUnico = usoUnico
        self.slot = slot
