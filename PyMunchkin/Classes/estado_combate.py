from Classes.estado import Estado


class Combate(Estado):
    def __init__(self):
        self.nome = "Combate"

    def executaFase(self):
        pass

    def get_EstadoDoJogo(self):
        return self.nome

