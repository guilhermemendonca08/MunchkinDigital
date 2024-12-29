from PPlay.gameimage import GameImage
from PPlay.window import Window


class UIHandler:
    def __init__(self, mouse):
        self.mouse = mouse

    def mouse_over_card(self, jogadores):
        selection = None
        for jogador in jogadores:
            for carta in jogador.mao:
                if self.mouse.is_over_object(carta.imagem):
                    # resolve carta sobrepostas pegando a última seleção
                    selection = carta
        return selection

    def mouse_over_object(self, objeto):
        if self.mouse.is_over_object(objeto):
            return True
        else:
            return False

