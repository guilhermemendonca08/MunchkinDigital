from Classes.estado import Estado


class ChutarPorta(Estado):
    def __init__(self):
        self.nome = "Chutar Porta"

    def executaFase(self):
        pass

    def get_faseDoJogo(self):
        return self.nome

