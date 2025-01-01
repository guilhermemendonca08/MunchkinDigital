from constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
    DOOR_HURTBOX_OFFSET_X,
    DOOR_HURTBOX_OFFSET_Y,
    TREASURE_JSON_DATA,
    DUNGEON_JSON_DATA,
)
from Classes.estado import Estado
from PPlay.gameimage import GameImage
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
        self.take_card = False
        self.unwrap_sfx = Sound(resource_path("Assets/SFX/tear_sound.ogg"))
        self.acc = 0
        self.mouse_state = False
        self.lock = False
        self.draw_sfx = Sound(resource_path("Assets/SFX/STS_SFX_CardDeal8_v1.ogg"))

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        self.acc += controlador.janela.delta_time()
        self.card_back.draw()

        if controlador.mouse_input.is_button_pressed(1):
            self.mouse_state = True

        if (
            controlador.mouse_input.is_button_pressed(1)
            and controlador.mouse_over_object(self.card_back)
            and not self.unwrap_card
        ):
            self.unwrap_card = True
            self.unwrap_sfx.play()
            print("aceitou carta")

        if not self.unwrap_card:
            self.card_back.set_position(
                RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
            )
            self.card_wrapper.set_position(
                RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
            )
            self.card_wrapper.draw()
            self.wrapper_top.set_position(
                RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
            )
            self.wrapper_bottom.set_position(
                RES_WIDTH / 2 - self.card_back.width / 2, RES_HEIGHT / 2
            )
        else:
            if self.acc > 0.01:
                # self.wrapper_bottom.y += 10
                if self.card_back.y > RES_HEIGHT / 2 - self.card_back.height / 2:
                    self.card_back.y -= 5
                self.wrapper_top.y -= 10
                self.acc = 0
            self.wrapper_bottom.draw()
            self.wrapper_top.draw()

        if (
            controlador.mouse_input.is_button_pressed(1)
            and controlador.mouse_over_object(self.card_back)
            and not self.take_card
            and self.card_back.y <= RES_HEIGHT / 2 - self.card_back.height / 2
        ):
            self.take_card = True

        if self.take_card and not self.lock:
            self.lock = True
            self.draw_sfx.play()
            nova_carta = controlador.comprar_carta(controlador.get_deck_dungeon())
            controlador.get_jogador_atual().add_card(nova_carta)
            self.reset()
            controlador.proximo_estado("Caridade")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
