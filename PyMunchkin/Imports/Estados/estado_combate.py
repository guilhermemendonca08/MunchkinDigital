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


class Combate(Estado):
    def __init__(self):
        self.nome = "Combate"
        self.mouse_state = False
        self.resolve_request = False
        self.cartas_aceitas = ["buff", "amplificador", "combate"]
        self.bgm = Sound(resource_path("Assets/SFX/wild_battle.ogg"))
        self.win_sfx = Sound(resource_path("Assets/SFX/battle_victory.ogg"))
        self.lose_sfx = Sound(resource_path("Assets/SFX/you_lost.ogg"))
        # self.lose_sfx = Sound(resource_path("Assets/SFX/battle_defeat.ogg"))
        self.battle_state = "DURING"  # DURING, WIN, LOSE
        self.opendoor = GameImage(resource_path("Assets/TableAssets/OpenDoor50.png"))
        self.opendoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        self.botao_resolve = Sprite(
            resource_path("Assets/TableAssets/sprite_resolver_combate.png"), 2
        )
        self.botao_resolve.set_position(
            RES_WIDTH - 1.5 * self.botao_resolve.width,
            RES_HEIGHT - 1.5 * self.botao_resolve.height,
        )
        self.botao_ir_para_caridade = Sprite(
            resource_path("Assets/TableAssets/sprite_ir_para_caridade.png"), 2
        )
        self.botao_ir_para_caridade.set_position(
            RES_WIDTH - 1.5 * self.botao_resolve.width,
            RES_HEIGHT - 1.5 * self.botao_resolve.height,
        )
        self.recompensas = []
        self.loot_recebido = GameImage(
            resource_path("Assets/TableAssets/loot_recebido.png")
        )
        self.you_lost = GameImage(resource_path("Assets/TableAssets/you_lost.png"))

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        self.opendoor.draw()
        monstro = controlador.get_carta_em_jogo()
        if self.battle_state == "DURING":
            monstro.set_position(
                RES_WIDTH / 2 - CARD_WIDTH / 2 - 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
            )
            monstro.draw()
            self.botao_resolve.draw()
            if controlador.mouse_over_object(self.botao_resolve):
                self.botao_resolve.set_curr_frame(1)
            else:
                self.botao_resolve.set_curr_frame(0)
            if self.bgm.is_playing() is False:
                self.bgm.set_repeat(True)
                self.bgm.set_volume(10)
                self.bgm.play()
            # Se clicou em Resolve Combate...
            if (
                not controlador.mouse_input.is_button_pressed(1)
                and self.mouse_state
                and controlador.mouse_over_object(self.botao_resolve)
            ):
                self.mouse_state = False
                controlador.discard_card(monstro)
                controlador.remove_carta_em_jogo()
                if controlador.get_resultado_combate():
                    # Recebe Tesouros
                    self.recompensas = []
                    for _ in range(monstro.get_qnt_tesouro()):
                        self.recompensas.append(
                            controlador.jogador_compra_carta(
                                controlador.get_jogador_atual(),
                                controlador.get_deck_tesouro(),
                            )
                        )
                    controlador.level_up(controlador.get_jogador_atual())
                    self.win_sfx.set_volume(20)
                    self.win_sfx.play()
                    self.battle_state = "WIN"
                else:
                    monstro.aplica_bad_stuff(controlador.get_jogador_atual())
                    self.lose_sfx.set_volume(20)
                    self.lose_sfx.play()
                    self.battle_state = "LOSE"
        else:
            controlador.finaliza_combate()
            self.bgm.stop()
            self.cartas_aceitas = []
            self.botao_ir_para_caridade.draw()
            if controlador.mouse_over_object(self.botao_ir_para_caridade):
                self.botao_ir_para_caridade.set_curr_frame(1)
            else:
                self.botao_ir_para_caridade.set_curr_frame(0)
            # Se clicou em Ir para Caridade...
            if (
                not controlador.mouse_input.is_button_pressed(1)
                and self.mouse_state
                and controlador.mouse_over_object(self.botao_ir_para_caridade)
            ):
                controlador.proximo_estado("Caridade")

        if self.battle_state == "WIN":
            # Exibir cartas recebidos da lista 'recompensas'
            self.loot_recebido.set_position(
                RES_WIDTH / 2 - self.loot_recebido.width / 2, RES_HEIGHT / 4
            )
            self.loot_recebido.draw()
            card_draw_offset_x = 0
            pixel_size_recompensas = CARD_WIDTH * len(self.recompensas)
            for each in self.recompensas:
                each.set_position(
                    RES_WIDTH / 2 - pixel_size_recompensas / 2 + card_draw_offset_x,
                    RES_HEIGHT / 2 - CARD_HEIGHT / 2,
                )
                each.draw()
                card_draw_offset_x += CARD_WIDTH

        if self.battle_state == "LOSE":
            self.you_lost.set_position(
                RES_WIDTH / 2 - self.you_lost.width / 2,
                RES_HEIGHT / 2 - self.you_lost.height / 2,
            )
            self.you_lost.draw()

        # Atualiza estado anterior do mouse
        if controlador.mouse_input.is_button_pressed(1):
            self.mouse_state = True
        else:
            self.mouse_state = False

        # if self.bgm.is_playing() is False:
        #     self.bgm.set_repeat(True)
        #     self.bgm.set_volume(10)
        #     self.bgm.play()
        # opendoor = GameImage(resource_path("Assets/TableAssets/OpenDoor50.png"))
        # opendoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        # opendoor.draw()
        #
        # controlador.get_carta_em_jogo().set_position(
        #     RES_WIDTH / 2 - CARD_WIDTH / 2 - 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
        # )
        # controlador.get_carta_em_jogo().draw()
        #
        # botao_resolve = Sprite(
        #     resource_path("Assets/TableAssets/sprite_resolver_combate.png"), 2
        # )
        # botao_resolve.set_position(
        #     RES_WIDTH - 1.5 * botao_resolve.width,
        #     RES_HEIGHT - 1.5 * botao_resolve.height,
        # )
        #
        # # Button Hover
        # target = controlador.mouse_over_object(botao_resolve)
        # if target:
        #     botao_resolve.set_curr_frame(1)
        # botao_resolve.draw()
        #
        # if controlador.mouse_input.is_button_pressed(1):
        #     self.mouse_state = True
        #
        # # sets button pressed flag
        # if (
        #     (self.mouse_state)
        #     and (not controlador.mouse_input.is_button_pressed(1))
        #     and (not self.resolve_request)  # Evita request duplo
        # ):
        #     self.mouse_state = False
        #     if target:
        #         self.resolve_request = True
        #         monstro = controlador.get_carta_em_jogo()
        #         if controlador.get_resultado_combate():
        #             # Recebe Tesouros
        #             for _ in range(monstro.get_qnt_tesouro()):
        #                 controlador.jogador_compra_carta(
        #                     controlador.get_jogador_atual(),
        #                     controlador.get_deck_tesouro(),
        #                 )
        #             # print("Jogador venceu")
        #             self.bgm.stop()
        #             controlador.level_up(controlador.get_jogador_atual())
        #             self.win_sfx.set_volume(20)
        #             self.win_sfx.play()
        #             controlador.discard_card(monstro)
        #             controlador.remove_carta_em_jogo()
        #             controlador.finaliza_combate()
        #             self.reset()
        #             controlador.proximo_estado("Caridade")
        #         else:
        #             # print("Monstro venceu")
        #             self.bgm.stop()
        #             monstro.aplica_bad_stuff(controlador.get_jogador_atual())
        #             self.lose_sfx.set_volume(20)
        #             self.lose_sfx.play()
        #             controlador.discard_card(monstro)
        #             controlador.remove_carta_em_jogo()
        #             controlador.finaliza_combate()
        #             self.reset()
        #             controlador.proximo_estado("Caridade")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
