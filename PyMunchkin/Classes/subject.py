from abc import ABC, abstractmethod
from Classes.observer import Observer


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, estado_do_jogo, jogador_atual, carta_em_jogo):
        pass
