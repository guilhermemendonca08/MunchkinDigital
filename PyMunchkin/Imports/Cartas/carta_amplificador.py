from Imports.Cartas.carta import Carta


class Amplificador(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deck_origem)

    def get_target_type(self):
        return ["monstro"]

    def jogar_carta(self, alvo):
        self.executar_efeito(alvo)

    def executar_efeito(self, alvo):
        self.efeito.aplicar_efeito(alvo)

