from random import choice


class Efeito:
    def aplicar_efeito(self, alvo):
        pass


# Done
class Buff(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        alvo.aplicar_buff(self.valor)


# Done
class AddToLevel(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        alvo.adiciona_ao_nivel_personagem(self.valor)


# Done
class DiscardCards(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        alvo.descarta_cartas(self.valor)


class DiscardGear(Efeito):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_efeito(self, alvo):
        gear_list = alvo.request_gear(self.valor)
        if gear_list:
            alvo.desequipar_item(choice(gear_list))
        # footgear
        # bigitem
        # any (card 69, 72)
        # smallitem?
        # 80


class DiscardRaca(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.discard_raca()


class DiscardClasse(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.discard_classe()


class Death(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.morrer()


class Equip(Efeito):  # Deprecated
    def aplicar_efeito(self, alvo):
        pass
        # print(f"{alvo.get_nome()} equipou  )

