class Efeito:
    def aplicar_efeito(self, alvo):
        pass


class Buff(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        alvo.aplicar_buff(self.valor)

    # def debug(self):
    #     return f"Buff: {self.valor}"


class AddToLevel(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        alvo.adiciona_ao_nivel_personagem(self.valor)


class DiscardGear(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        pass


class DiscardCards(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        pass


class DiscardRaca(Efeito):

    def aplicar_efeito(self, alvo):
        alvo.discard_raca()


class DiscardClasse(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.discard_classe()


class Death(Efeito):
    def aplicar_efeito(self, alvo):
        pass


class Equip(Efeito):  # Deprecated
    def aplicar_efeito(self, alvo):
        pass
        # print(f"{alvo.get_nome()} equipou  )

