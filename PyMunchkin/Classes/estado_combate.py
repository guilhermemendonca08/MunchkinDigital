from constants import (
    RES_WIDTH,
    RES_HEIGHT,
    DOOR_HURTBOX_OFFSET_X,
    DOOR_HURTBOX_OFFSET_Y,
    CARD_WIDTH,
    CARD_HEIGHT,
)
from Classes.estado import Estado
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite


class Combate(Estado):
    def __init__(self):
        self.nome = "Combate"
        self.mouse_click = False
        self.resolve_request = False
        self.cartas_aceitas = ["buff"]

    def executa_fase(self, controlador):
        closeddoor = GameImage("Assets/TableAssets/OpenDoor50.png")
        closeddoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        closeddoor.draw()

        controlador.get_carta_em_jogo().set_position(
            RES_WIDTH / 2 - CARD_WIDTH / 2 - 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
        )
        controlador.get_carta_em_jogo().draw()

        botao_resolve = Sprite("Assets/TableAssets/ButtonSpriteHighlight.png", 2)
        botao_resolve.set_position(
            RES_WIDTH - 1.5 * botao_resolve.width,
            RES_HEIGHT - 1.5 * botao_resolve.height,
        )

        # Button Hover
        target = controlador.mouse_over_object(botao_resolve)
        if target:
            botao_resolve.set_curr_frame(1)
        botao_resolve.draw()

        if controlador.mouse_input.is_button_pressed(1):
            self.mouse_click = True

        # sets button pressed flag
        if (
            (self.mouse_click)
            and (not controlador.mouse_input.is_button_pressed(1))
            and (not self.resolve_request)  # Evita request duplo
        ):
            self.mouse_click = False
            if target:
                self.resolve_request = True
                print("Clicou botao")
                # LEMBRETE: Aqui o gerenciadorcombate seria chamado
                # mas agora vo parar para fazer sistema de equipar e
                # o método de calcular força do jogador e monstro.
                # Porque são pre-requisitos para o gerenciador de combate.

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas or (
            carta.get_tipo() == "item" and carta.get_uso_unico()
        ):
            return True
        else:
            return False
