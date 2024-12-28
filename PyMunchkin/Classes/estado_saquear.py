from Classes.estado import Estado


class Saquear(Estado):
    def __init__(self):
        self.nome = "Saquear"

    def executaFase(self):
        pass

    def get_EstadoDoJogo(self):
        return self.nome

