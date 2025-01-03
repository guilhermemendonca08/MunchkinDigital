from abc import ABC, abstractmethod
from Imports.observer import Observer


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, estado_do_jogo, jogador_ativo, carta_em_jogo):
        pass

