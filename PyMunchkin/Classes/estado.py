from abc import ABC, abstractmethod


class Estado(ABC):
    @abstractmethod
    def executaFase(self, controlador):
        pass

    @abstractmethod
    def get_EstadoDoJogo(self) -> str:
        pass
