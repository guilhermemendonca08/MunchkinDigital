from Classes.estado import Estado


class Caridade(Estado):
    def __init__(self):
        self.nome = "Caridade"
        self.cartas_aceitas = [
            "maldicao",
            "classe",
            "raca",
            "equipamento",
            "utilitario",
        ]

    def executa_fase(self, controlador):
        pass
        # print("Caridade")
        # controlador.proximo_turno()
        # controlador.proximo_estado("ChutarPorta")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
