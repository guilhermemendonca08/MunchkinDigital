from Classes.carta import Carta


class Maldicao(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
        duracao,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deck_origem)
        self.duracao = duracao

    def jogar_carta(self, alvo):
        self.executar_efeito(alvo)

    def executar_efeito(self, alvo):
        print(f"{alvo.get_nome()} sofreu {self.get_nome()}")
        self.efeito.aplicar_efeito(alvo)

    def get_target_type(self):
        return ["jogador"]

