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
        self.new_card = None

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

        if controlador.mouse_input.is_button_pressed(1):
            self.mouse_click = True

        # sets timer for animation, flags door kick variable
        if (
            (self.mouse_click)
            and (not controlador.mouse_input.is_button_pressed(1))
            and (not self.door_kicked)  # Evita abrir a porta duas vezes.
        ):
            self.mouse_click = False
            if target:
                self.door_kicked = True
                print("chutou porta")
                self.acc = 0

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
