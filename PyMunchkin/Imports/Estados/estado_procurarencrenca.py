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


class ProcurarEncrenca(
    Estado,
):
    def __init__(self):
        self.nome = "Procurar Encrenca"
        # self.cartas_aceitas = ["monstro"]
        self.cartas_aceitas = []
        self.bgm = Sound(resource_path(resource_path("Assets/SFX/item_catch.ogg")))
        self.intro = True
        self.accept_card = False
        self.loot_button = Sprite(
            resource_path("Assets/TableAssets/sprite_saquear_sala.png"), 2
        )

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        if self.bgm.is_playing() == False and self.intro:
            self.bgm.set_volume(20)
            self.bgm.play()
            self.intro = False
        opendoor = GameImage(resource_path("Assets/TableAssets/OpenDoor50.png"))
        opendoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        opendoor.draw()
        spotlights = GameImage(resource_path("Assets/TableAssets/spotlights3.png"))
        spotlights.set_position(
            RES_WIDTH / 2 - spotlights.width / 2, RES_HEIGHT / 2 - spotlights.height / 2
        )
        spotlights.draw()

        if not self.accept_card:
            revealed_card = controlador.get_carta_em_jogo()
            revealed_card.set_position(
                RES_WIDTH / 2 - CARD_WIDTH / 2 - 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
            )
            revealed_card.draw()

            if controlador.detect_exact_choice([revealed_card]):
                self.accept_card = True
                # Se for maldicão, joga em si mesmo.
                if revealed_card.get_tipo() == "maldicao":
                    controlador.get_jogador_ativo().add_card(revealed_card)
                    self.cartas_aceitas.append("maldicao")
                    # controlador.get_jogador_atual().jogar_carta(
                    #     revealed_card, controlador.get_jogador_atual()
                    # )
                    controlador.play_attempt(
                        revealed_card, target=controlador.get_jogador_ativo()
                    )
                    self.cartas_aceitas.remove("maldicao")

                else:
                    controlador.get_jogador_ativo().add_card(revealed_card)
                controlador.remove_carta_em_jogo()
                self.cartas_aceitas.append("monstro")
        else:

            self.loot_button.set_position(
                RES_WIDTH - 1.5 * self.loot_button.width,
                RES_HEIGHT - 1.5 * self.loot_button.height,
            )

            # Button Hover
            target = controlador.mouse_over_object(self.loot_button)
            if target:
                self.loot_button.set_curr_frame(1)
            else:
                self.loot_button.set_curr_frame(0)
            self.loot_button.draw()

            if controlador.mouse_input.is_button_pressed(1) and target and controlador.is_their_turn():
                self.reset()
                controlador.proximo_estado("Saquear")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
