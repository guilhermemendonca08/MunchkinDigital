from Classes.estado import Estado


class ProcurarEncrenca(Estado):
    def __init__(self):
        self.nome = "Procurar Encrenca"

    def executaFase(self):
        pass

    def get_faseDoJogo(self):
        return self.nome

