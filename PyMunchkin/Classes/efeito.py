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


class AddToLevel(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicarEfeito(self, alvo):
        alvo.adicionaAoNivelPersonagem(self.valor)


class DiscardGear(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicarEfeito(self, alvo):
        pass


class DiscardCards(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicarEfeito(self, alvo):
        pass


class DiscardRaca(Efeito):

    def aplicarEfeito(self, alvo):
        alvo.discard_raca()


class DiscardClasse(Efeito):
    def aplicarEfeito(self, alvo):
        alvo.discard_classe()


class Death(Efeito):
    def aplicarEfeito(self, alvo):
        pass


class Equip(Efeito):  # Deprecated
    def aplicarEfeito(self, alvo):
        pass
        # print(f"{alvo.get_nome()} equipou  )

