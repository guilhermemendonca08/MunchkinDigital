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


class Combate(Estado):
    def __init__(self):
        self.nome = "Combate"

    def executaFase(self, controlador):
        closeddoor = GameImage("Assets/TableAssets/OpenDoor50.png")
        closeddoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
        closeddoor.draw()

        controlador.get_cartaEmJogo().set_position(
            RES_WIDTH / 2 - CARD_WIDTH/2 - 2, RES_HEIGHT / 2 - CARD_HEIGHT / 2
        )
        controlador.get_cartaEmJogo().draw()

    def get_EstadoDoJogo(self):
        return self.nome
