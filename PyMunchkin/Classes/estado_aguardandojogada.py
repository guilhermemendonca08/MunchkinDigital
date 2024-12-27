from Classes.estado import Estado


class AguardandoJogada(Estado):
    def __init__(self):
        self.nome = "Aguardando Jogada"

    def executaFase(self):
        pass

    def get_faseDoJogo(self):
        return self.nome

