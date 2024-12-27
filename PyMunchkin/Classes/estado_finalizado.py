from Classes.estado import Estado


class Finalizado(Estado):
    def __init__(self):
        self.nome = "Finalizado"

    def executaFase(self):
        pass

    def get_faseDoJogo(self):
        return self.nome

