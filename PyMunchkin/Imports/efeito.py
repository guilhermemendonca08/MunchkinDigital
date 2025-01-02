from abc import ABC, abstractmethod
from random import choice


class Efeito(ABC):
    @abstractmethod
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


# Done
class DiscardGear(Efeito):
    def __init__(self, valor, quantidade=None):
        self.valor = valor
        self.quantidade = quantidade

    def aplicar_efeito(self, alvo):
        if self.quantidade is None:
            self.quantidade = 1

        gear_list = alvo.request_gear(self.valor)
        for _ in range(self.quantidade):
            if gear_list:
                alvo.desequipar_item(choice(gear_list))
                gear_list = alvo.request_gear(self.valor)


# Done
class DiscardRaca(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.discard_raca()


# Done
class DiscardClasse(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.discard_classe()


# Done
class Death(Efeito):
    def aplicar_efeito(self, alvo):
        alvo.morrer()


# efeito nao conhece 'carta' para pedir para o jogador equipar 'carta'
class Equip(Efeito):  # Deprecated
    def aplicar_efeito(self, alvo):
        pass
        # print(f"{alvo.get_nome()} equipou  )

