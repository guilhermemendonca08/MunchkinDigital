from Imports.constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
)
from Imports.Estados.estado import Estado
from PPlay.gameimage import GameImage
from path import resource_path
from PPlay.sprite import Sprite

# from PPlay.sound import Sound


class Caridade(Estado):
    def __init__(self):
        self.nome = "Caridade"
        self.cartas_aceitas = [
            "maldicao",
            "classe",
            "raca",
            "equipamento",
            "utilitario",
        ]
        self.mouse_state = False
        self.bg = GameImage(
            resource_path(resource_path("Assets/TableAssets/carta_caridade_alt.png"))
        )
        self.bg.set_position(
            RES_WIDTH / 2 - self.bg.width / 2, RES_HEIGHT / 2 - self.bg.height / 2
        )
        self.botao_ir_para_caridade = Sprite(
            resource_path("Assets/TableAssets/sprite_doar_excedentes.png"), 2
        )
        self.botao_ir_para_caridade.set_position(
            RES_WIDTH - 1.5 * self.botao_ir_para_caridade.width,
            RES_HEIGHT - 1.5 * self.botao_ir_para_caridade.height,
        )

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        self.bg.draw()
        self.botao_ir_para_caridade.draw()
        if controlador.mouse_over_object(self.botao_ir_para_caridade):
            self.botao_ir_para_caridade.set_curr_frame(1)
        else:
            self.botao_ir_para_caridade.set_curr_frame(0)

        if (
            not controlador.mouse_input.is_button_pressed(1)
            and self.mouse_state
            and controlador.mouse_over_object(self.botao_ir_para_caridade)
        ):

            self.mouse_state = False
            # Doa cartas excedentes
            controlador.proximo_estado("ChutarPorta")

        # controlador.proximo_turno()
        # controlador.proximo_estado("ChutarPorta")

        # Atualiza estado anterior do mouse
        if controlador.mouse_input.is_button_pressed(1):
            self.mouse_state = True
        else:
            self.mouse_state = False

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
