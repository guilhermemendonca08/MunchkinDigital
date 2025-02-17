from Imports.constants import (
    RES_WIDTH,
    RES_HEIGHT,
    DOOR_HURTBOX_OFFSET_X,
    DOOR_HURTBOX_OFFSET_Y,
    CARD_WIDTH,
    CARD_HEIGHT,
)
from Imports.Estados.estado import Estado
from PPlay.gameimage import GameImage
from PPlay.sound import Sound
from path import resource_path


class ChutarPorta(Estado):
    def __init__(self):
        self.nome = "Chutar Porta"
        self.mouse_click = False
        self.door_kicked = False
        self.carddrawn = False
        self.buildup = Sound(resource_path("Assets/SFX/buildup.ogg"))
        self.door_knock = Sound(resource_path("Assets/SFX/door_knock.ogg"))
        self.acc = 0
        self.cardanimation = GameImage(
            resource_path("Assets/Door/000 (small)discard.png")
        )
        self.cardanimation.set_position(
            RES_WIDTH - 2.5 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
        )
        self.cartas_aceitas = [
            "maldicao",
            "classe",
            "raca",
            "equipamento",
            "utilitario",
        ]

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        if not controlador.get_jogador_ativo().esta_vivo():
            for _ in range(4):
                controlador.get_jogador_ativo().add_card(
                    controlador.comprar_carta(controlador.deck_tesouro)
                )
            for _ in range(4):
                controlador.get_jogador_ativo().add_card(
                    controlador.comprar_carta(controlador.deck_dungeon)
                )
            controlador.revive_jogador(controlador.get_jogador_ativo())
        self.acc += controlador.janela.delta_time()
        # cardanimation = GameImage("Assets/Door/000 (small)discard.png")
        closeddoor = GameImage(resource_path("Assets/TableAssets/ClosedDoor50.png"))
        closeddoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        closeddoor.draw()

        doorhurtbox = GameImage(
            resource_path("Assets/TableAssets/DoorHurtBoxTransparent.png")
        )
        doorhurtbox.set_position(
            RES_WIDTH / 4 + DOOR_HURTBOX_OFFSET_X,
            RES_HEIGHT / 4 + DOOR_HURTBOX_OFFSET_Y,
        )
        doorhurtbox.draw()

        # Door hover/click detection
        target = controlador.mouse_over_object(doorhurtbox)

        if controlador.is_mouse_left_click_pressed():
            self.mouse_click = True

        if (self.mouse_click) and (not controlador.is_mouse_left_click_pressed()):
            self.mouse_click = False

            if target and (not self.door_kicked) and controlador.is_their_turn():
                self.door_kicked = True
                # print("chutou porta")
                self.acc = 0

        # new card draw
        if self.door_kicked and not self.carddrawn:
            if self.buildup.is_playing() is False:
                self.buildup.set_volume(20)
                self.buildup.play()
                self.door_knock.set_volume(50)
                self.door_knock.play()
            self.intro = False
            self.carddrawn = True
            controlador.coloca_carta_em_jogo(
                controlador.comprar_carta(controlador.deck_dungeon)
            )
            # print(f"Carta nova: {controlador.get_cartaEmJogo().get_nome()}")

        # card draw animation
        if self.door_kicked:
            if self.cardanimation.x >= RES_WIDTH / 2 - CARD_WIDTH / 2:
                if self.acc > 0.005:
                    self.cardanimation.x -= 10
                    self.acc = 0
                self.cardanimation.draw()
            else:
                if controlador.get_carta_em_jogo().get_tipo() == "monstro":
                    controlador.proximo_estado("Combate")
                else:
                    controlador.proximo_estado("ProcurarEncrenca")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
