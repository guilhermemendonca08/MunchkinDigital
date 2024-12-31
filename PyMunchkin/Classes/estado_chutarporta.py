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


class ChutarPorta(Estado):
    def __init__(self):
        self.nome = "Chutar Porta"
        self.mouse_click = False
        self.door_kicked = False
        self.carddrawn = False
        self.acc = 0
        self.cardanimation = GameImage("Assets/Door/000 (small)discard.png")
        self.cardanimation.set_position(
            RES_WIDTH - 2.5 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
        )
        self.cartas_aceitas = ["maldicao", "classe", "raca"]

    def executaFase(self, controlador):
        self.acc += controlador.janela.delta_time()
        # cardanimation = GameImage("Assets/Door/000 (small)discard.png")
        closeddoor = GameImage("Assets/TableAssets/ClosedDoor50.png")
        closeddoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        closeddoor.draw()

        doorhurtbox = GameImage("Assets/TableAssets/DoorHurtBoxSemiTransparent.png")
        doorhurtbox.set_position(
            RES_WIDTH / 4 + DOOR_HURTBOX_OFFSET_X,
            RES_HEIGHT / 4 + DOOR_HURTBOX_OFFSET_Y,
        )
        doorhurtbox.draw()

        # Door hover/click detection
        target = controlador.mouse_over_object(doorhurtbox)

        # playtarget = controlador.mouse_over_card()

        # if controlador.mouse_input.is_button_pressed(1):
        if controlador.is_mouse_left_click_pressed():
            self.mouse_click = True

        if (self.mouse_click) and (not controlador.is_mouse_left_click_pressed()):
            self.mouse_click = False

            if target and (not self.door_kicked):
                self.door_kicked = True
                print("chutou porta")
                self.acc = 0

            # if playtarget:
            #     if controlador.get_jogadorAtual().has_card(playtarget):
            #         print(f"I play {playtarget.get_nome()}!")
            #         controlador.get_jogadorAtual().remove_card(playtarget)
            #     else:
            #         print(f"{playtarget.get_descricao()}")

        # new card draw
        if self.door_kicked and not self.carddrawn:
            self.carddrawn = True
            controlador.colocaCartaEmJogo(
                controlador.comprarCarta(controlador.deckDungeon)
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
                if controlador.get_cartaEmJogo().get_tipo() == "monstro":
                    controlador.proximoEstado("Combate")
                else:
                    controlador.proximoEstado("ProcurarEncrenca")

    def get_EstadoDoJogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas or (
            carta.get_tipo() == "item" and not carta.get_usoUnico()
        ):
            return True
        else:
            return False
