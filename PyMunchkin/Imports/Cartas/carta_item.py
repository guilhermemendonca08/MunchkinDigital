from Imports.Cartas.carta import Carta


class Item(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
        poder,
        tamanho,
        valor,
        restricao,
        uso_unico,
        slot,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deck_origem)
        self.poder = poder
        self.tamanho = tamanho
        self.valor = valor
        self.restricao = restricao
        self.uso_unico = uso_unico
        self.slot = slot

    def debug(self):
        super().debug()
        print(f"Poder: {self.poder}")
        print(f"Tamanho: {self.tamanho}")
        print(f"Valor: {self.valor}")
        print(f"Restrição: {self.restricao}")
        print(f"Uso único: {self.uso_unico}")
        print(f"Slot: {self.slot}")

    def get_poder(self):
        return self.poder

    def get_uso_unico(self):
        return self.uso_unico

    def jogar_carta(self, alvo):
        if self.tipo == "equipamento":
            alvo.equipar_item(self)
        else:
            self.efeito.aplicar_efeito(alvo)

    def executar_efeito(self, alvo):
        self.efeito.aplicar_efeito(alvo)

    def get_slot(self):
        return self.slot

    def get_target_type(self):
        if self.tipo == "combate":
            return ["combatentes"]
        if self.tipo == "utilitario":
            return ["jogador"]
