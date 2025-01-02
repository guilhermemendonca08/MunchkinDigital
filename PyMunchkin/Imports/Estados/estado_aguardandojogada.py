from Imports.Estados.estado import Estado


class AguardandoJogada(Estado):
    def __init__(self):
        self.nome = "Aguardando Jogada"

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        pass

    def get_estado_do_jogo(self):
        return self.nome

