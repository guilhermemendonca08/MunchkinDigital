from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, estado_do_jogo, jogador_atual, carta_em_jogo):
        pass

