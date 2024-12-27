from abc import ABC, abstractmethod


class Estado(ABC):
    @abstractmethod
    def executaFase(self):
        pass

    @abstractmethod
    def get_faseDoJogo(self, controlador):
        pass

