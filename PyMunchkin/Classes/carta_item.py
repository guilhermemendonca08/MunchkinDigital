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

    def debug(self):
        super().debug()
        print(f"Poder: {self.poder}")
        print(f"Tamanho: {self.tamanho}")
        print(f"Valor: {self.valor}")
        print(f"Restrição: {self.restricao}")
        print(f"Uso único: {self.usoUnico}")
        print(f"Slot: {self.slot}")

    def get_usoUnico(self):
        return self.usoUnico

    def executarEfeito(self, alvo):
        if not self.usoUnico:
            print(f"{alvo.get_nome()} equipou {self.get_nome()}")
            # alvo.equparItem(self)
        if not self.usoUnico:
            self.efeito.aplicarEfeito(alvo)
