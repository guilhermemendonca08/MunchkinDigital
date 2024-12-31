from Classes.carta import Carta


class Raca(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
        nome_raca,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deck_origem)
        self.nome_raca = nome_raca

    def get_nome_raca(self):
        return self.nome_raca

    def jogar_carta(self, alvo):
        print(f"{alvo.get_nome()} equipou {self.nome_raca}")
        alvo.equipar_raca(self)

