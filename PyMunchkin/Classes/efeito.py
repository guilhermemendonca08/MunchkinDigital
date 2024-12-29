class Efeito:
    def aplicarEfeito(self, alvo):
        pass


class Buff(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicarEfeito(self, alvo):
        alvo.mudarForcaCombate(self.valor)

    # def debug(self):
    #     return f"Buff: {self.valor}"

