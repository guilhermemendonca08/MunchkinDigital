from Classes.estado import Estado


class Saquear(Estado):
    def __init__(self):
        self.nome = "Saquear"

    def executaFase(self):
        pass

    def get_faseDoJogo(self):
        return self.nome

