from Imports.constants import RES_WIDTH, RES_HEIGHT
from Imports.Estados.estado import Estado
from PPlay.gameimage import GameImage
from path import resource_path


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
        # self.bg = GameImage(
        #     resource_path(resource_path("Assets/TableAssets/charity.png"))
        # )
        self.bg = GameImage(
            resource_path(resource_path("Assets/TableAssets/carta_caridade_alt.png"))
        )
        self.bg.set_position(
            RES_WIDTH / 2 - self.bg.width / 2, RES_HEIGHT / 2 - self.bg.height / 2
        )

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        self.bg.draw()
        # controlador.proximo_turno()
        # controlador.proximo_estado("ChutarPorta")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
