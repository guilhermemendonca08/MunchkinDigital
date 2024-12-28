from Classes.estado import Estado


class Fuga(Estado):
    def __init__(self):
        self.nome = "Fuga"

    def executaFase(self):
        pass

    def get_EstadoDoJogo(self):
        return self.nome

