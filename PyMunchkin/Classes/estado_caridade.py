from Classes.estado import Estado


class Caridade(Estado):
    def __init__(self):
        self.nome = "Caridade"

    def executa_fase(self):
        pass

    def get_estado_do_jogo(self):
        return self.nome

