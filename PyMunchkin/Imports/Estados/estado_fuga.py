from Imports.Estados.estado import Estado


class Fuga(Estado):
    def __init__(self):
        self.nome = "Fuga"

    def executa_fase(self):
        pass

    def get_estado_do_jogo(self):
        return self.nome

