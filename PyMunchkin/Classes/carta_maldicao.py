from Classes.carta import Carta


class Maldicao(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deckOrigem,
        duracao,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deckOrigem)
        self.duracao = duracao

    def jogarCarta(self, alvo):
        self.executarEfeito(alvo)

    def executarEfeito(self, alvo):
        print(f"{alvo.get_nome()} sofreu {self.get_nome()}")
        self.efeito.aplicarEfeito(alvo)

    def get_target_type(self):
        return ["jogador"]

