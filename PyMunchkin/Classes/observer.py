from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, estado_do_jogo: str):
        pass

