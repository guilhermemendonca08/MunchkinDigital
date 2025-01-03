from Imports.constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
)
from Imports.Estados.estado import Estado
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.sound import Sound
from path import resource_path


class Saquear(Estado):
    def __init__(self):
        self.nome = "Saquear"
        self.cartas_aceitas = []
        self.card_pack = GameImage(
            resource_path("Assets/TableAssets/booster_with_card.png")
        )
        self.card_back = GameImage(
            resource_path("Assets/TableAssets/booster_door_card.png")
        )
        self.card_wrapper = GameImage(
            resource_path("Assets/TableAssets/booster_wrapper.png")
        )
        self.wrapper_bottom = GameImage(
            resource_path("Assets/TableAssets/booster_ripped_bottom.png")
        )
        self.wrapper_top = GameImage(
            resource_path("Assets/TableAssets/booster_ripped_top.png")
        )
        self.unwrap_card = False
        self.unwrap_sfx = Sound(resource_path("Assets/SFX/tear_sound.ogg"))
        self.acc = 0
        self.mouse_state = False
        self.draw_sfx = Sound(resource_path("Assets/SFX/sfx_card_deal.ogg"))
        self.display_state = "WRAPPED"  # WRAPPED, UNWRAPPING, UNWRAPPED, DISPLAY LOOT
        self.wrapper_top.set_position(
            RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
        )
        self.wrapper_bottom.set_position(
            RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
        )
        self.botao_ir_para_caridade = Sprite(
            resource_path("Assets/TableAssets/sprite_ir_para_caridade.png"), 2
        )
        self.botao_ir_para_caridade.set_position(
            RES_WIDTH - 1.5 * self.botao_ir_para_caridade.width,
            RES_HEIGHT - 1.5 * self.botao_ir_para_caridade.height,
        )
        self.mensagem_loot_recebido = GameImage(
            resource_path("Assets/TableAssets/loot_recebido.png")
        )
        self.nova_carta = None

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        self.acc += controlador.janela.delta_time()

        if self.display_state == "WRAPPED":
            self.card_back.draw()
            self.card_back.set_position(
                RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
            )
            self.card_wrapper.set_position(
                RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
            )
            self.card_wrapper.draw()

            # Clicou na carta?
            if (
                not controlador.mouse_input.is_button_pressed(1)
                and self.mouse_state
                and controlador.mouse_over_object(self.card_back)
            ):
                self.display_state = "UNWRAPPING"
                self.unwrap_sfx.play()

        if self.display_state == "UNWRAPPING":
            self.card_back.draw()
            self.wrapper_bottom.draw()
            self.wrapper_top.draw()
            if self.acc > 0.01:
                self.wrapper_top.y -= 10
                self.acc = 0
                if self.card_back.y > RES_HEIGHT / 2 - self.card_back.height / 2:
                    self.card_back.y -= 5
                elif self.wrapper_top.y < -100:
                    self.display_state = "UNWRAPPED"
        if self.display_state == "UNWRAPPED":
            self.card_back.draw()
            self.wrapper_bottom.draw()

            # Clicou na carta?
            if (
                not controlador.mouse_input.is_button_pressed(1)
                and self.mouse_state
                and controlador.mouse_over_object(self.card_back)
            ):
                self.mouse_state = False
                self.draw_sfx.play()
                self.nova_carta = controlador.comprar_carta(
                    controlador.get_deck_dungeon()
                )
                controlador.get_jogador_ativo().add_card(self.nova_carta)
                self.display_state = "DISPLAY LOOT"
        if self.display_state == "DISPLAY LOOT":
            self.botao_ir_para_caridade.draw()
            if controlador.mouse_over_object(self.botao_ir_para_caridade):
                self.botao_ir_para_caridade.set_curr_frame(1)
            else:
                self.botao_ir_para_caridade.set_curr_frame(0)
            self.mensagem_loot_recebido.set_position(
                RES_WIDTH / 2 - self.mensagem_loot_recebido.width / 2, RES_HEIGHT / 4
            )
            self.mensagem_loot_recebido.draw()
            self.nova_carta.set_position(
                RES_WIDTH / 2 - CARD_WIDTH / 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
            )
            self.nova_carta.draw()
            if (
                not controlador.mouse_input.is_button_pressed(1)
                and self.mouse_state
                and controlador.mouse_over_object(self.botao_ir_para_caridade)
            ):
                controlador.proximo_estado("Caridade")

        # if (
        #     not controlador.mouse_input.is_button_pressed(1)
        #     and self.mouse_state
        #     and controlador.mouse_over_object(self.card_back)
        #     and not self.unwrap_card
        # ):
        #     self.unwrap_card = True
        #     self.unwrap_sfx.play()
        #     # print("aceitou carta")
        #
        # # Card Unwrap animation
        # if not self.unwrap_card:
        #     self.card_back.set_position(
        #         RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
        #     )
        #     self.card_wrapper.set_position(
        #         RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
        #     )
        #     self.card_wrapper.draw()
        #     self.wrapper_top.set_position(
        #         RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
        #     )
        #     self.wrapper_bottom.set_position(
        #         RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
        #     )
        # else:
        #     if self.acc > 0.01:
        #         # self.wrapper_bottom.y += 10
        #         if self.card_back.y > RES_HEIGHT / 2 - self.card_back.height / 2:
        #             self.card_back.y -= 5
        #         self.wrapper_top.y -= 10
        #         self.acc = 0
        #     self.wrapper_bottom.draw()
        #     self.wrapper_top.draw()
        #
        # if (
        #     controlador.mouse_input.is_button_pressed(1)
        #     and controlador.mouse_over_object(self.card_back)
        #     and not self.take_card
        #     and self.card_back.y <= RES_HEIGHT / 2 - self.card_back.height / 2
        # ):
        #     self.take_card = True
        #
        # if self.take_card and not self.lock:
        #     self.lock = True
        #     self.draw_sfx.play()
        #     nova_carta = controlador.comprar_carta(controlador.get_deck_dungeon())
        #     controlador.get_jogador_atual().add_card(nova_carta)
        #     self.reset()
        #     controlador.proximo_estado("Caridade")
        #
        # # Atualiza estado anterior do mouse
        # if controlador.mouse_input.is_button_pressed(1):
        #     self.mouse_state = True
        # else:
        #     self.mouse_state = False

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
