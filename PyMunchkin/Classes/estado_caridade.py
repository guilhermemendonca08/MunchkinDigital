from Classes.estado import Estado


class Caridade(Estado):
    def __init__(self):
        self.nome = "Caridade"

    def executa_fase(self, controlador):
        print("Caridade")
        controlador.proximo_turno()
        controlador.proximo_estado("ChutarPorta")

    def get_estado_do_jogo(self):
        return self.nome
