from Classes.estado import Estado


class Saquear(Estado):
    def __init__(self):
        self.nome = "Saquear"

    def executa_fase(self, controlador):
        pass

    def get_estado_do_jogo(self):
        return self.nome
