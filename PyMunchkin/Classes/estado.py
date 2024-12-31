from abc import ABC, abstractmethod


class Estado(ABC):
    @abstractmethod
    def executa_fase(self, controlador):
        pass

    @abstractmethod
    def get_estado_do_jogo(self) -> str:
        pass
