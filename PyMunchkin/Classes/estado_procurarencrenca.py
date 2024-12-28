from Classes.estado import Estado


class ProcurarEncrenca(
    Estado,
):
    def __init__(self):
        self.nome = "Procurar Encrenca"

    def executaFase(self, controlador):
        pass

    def get_EstadoDoJogo(self):
        return self.nome
