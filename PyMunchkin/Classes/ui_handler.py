from PPlay.gameimage import GameImage
from PPlay.window import Window


class UIHandler:
    def __init__(self, mouse, controladorJogo):
        self.controlador = controladorJogo
        self.mouse = mouse

    def mouse_over_card(self):
        selection = None
        for jogador in self.controlador.jogadores:
            for carta in jogador.mao:
                if self.mouse.is_over_object(carta.imagem):
                    # resolve carta sobrepostas pegando a última seleção
                    selection = carta
        return selection

