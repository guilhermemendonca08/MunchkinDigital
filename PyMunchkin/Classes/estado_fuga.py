from Classes.estado import Estado


class Fuga(Estado):
    def __init__(self):
        self.nome = "Fuga"

    def executaFase(self):
        pass

    def get_faseDoJogo(self):
        return self.nome

