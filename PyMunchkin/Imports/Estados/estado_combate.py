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
        self.mouse_click = False
        self.resolve_request = False
        self.cartas_aceitas = ["buff", "amplificador", "combate"]
        self.bgm = Sound(resource_path("Assets/SFX/wild_battle.ogg"))
        self.win_sfx = Sound(resource_path("Assets/SFX/fanfare.ogg"))
        self.lose_sfx = Sound(resource_path("Assets/SFX/you_died.ogg"))

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        if self.bgm.is_playing() == False:
            self.bgm.set_repeat(True)
            self.bgm.set_volume(10)
            self.bgm.play()
        opendoor = GameImage(resource_path("Assets/TableAssets/OpenDoor50.png"))
        opendoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        opendoor.draw()

        controlador.get_carta_em_jogo().set_position(
            RES_WIDTH / 2 - CARD_WIDTH / 2 - 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
        )
        controlador.get_carta_em_jogo().draw()

        botao_resolve = Sprite(
            resource_path("Assets/TableAssets/ButtonSpriteHighlight.png"), 2
        )
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
                monstro = controlador.get_carta_em_jogo()
                if controlador.get_resultado_combate():
                    # Recebe Tesouros
                    for _ in range(monstro.get_qnt_tesouro()):
                        controlador.jogador_compra_carta(
                            controlador.get_jogador_atual(),
                            controlador.get_deck_tesouro(),
                        )
                    # print("Jogador venceu")
                    self.bgm.stop()
                    controlador.level_up(controlador.get_jogador_atual())
                    self.win_sfx.set_volume(20)
                    self.win_sfx.play()
                    controlador.discard_card(monstro)
                    controlador.remove_carta_em_jogo()
                    controlador.finaliza_combate()
                    self.reset()
                    controlador.proximo_estado("Caridade")
                else:
                    # print("Monstro venceu")
                    self.bgm.stop()
                    monstro.aplica_bad_stuff(controlador.get_jogador_atual())
                    self.lose_sfx.set_volume(20)
                    self.lose_sfx.play()
                    controlador.discard_card(monstro)
                    controlador.remove_carta_em_jogo()
                    controlador.finaliza_combate()
                    self.reset()
                    controlador.proximo_estado("Caridade")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False