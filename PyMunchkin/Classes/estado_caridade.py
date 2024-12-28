from Classes.estado import Estado


class Caridade(Estado):
    def __init__(self):
        self.nome = "Caridade"

    def executaFase(self):
        pass

    def get_EstadoDoJogo(self):
        return self.nome

