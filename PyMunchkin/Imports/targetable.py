from abc import ABC, abstractmethod


class Targetable(ABC):
    @abstractmethod
    def aplicar_buff(self, valor):
        pass

    @abstractmethod
    def reseta_buffs(self):
        pass

