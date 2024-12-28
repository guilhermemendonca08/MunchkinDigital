from Classes.estado import Estado


class ChutarPorta(Estado):
    def __init__(self):
        self.nome = "Chutar Porta"

    def executaFase(self, controlador):
        pass

    def get_EstadoDoJogo(self):
        return self.nome
