from Classes.carta import Carta


class Raca(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        nomeRaca,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.nomeRaca = nomeRaca

    def get_nome_raca(self):
        return self.nomeRaca

    def executarEfeito(self, alvo):
        print(f"{alvo.get_nome()} equipou {self.nomeRaca}")
        alvo.equiparRaca(self)

