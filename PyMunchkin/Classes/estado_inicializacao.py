from Classes.estado import Estado


class Inicializacao(Estado):
    def __init__(self):
        self.nome = "Inicializacao"

    def executaFase(self, controlador):
        # print("Executando fase", controlador.get_estadoDoJogo())
        pass

    def get_faseDoJogo(self):
        return self.nome

