from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, estado_do_jogo, jogador_ativo, carta_em_jogo):
        pass

