from Imports.Cartas.carta import Carta


class Classe(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
        nome_classe,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deck_origem)
        self.nome_classe = nome_classe

    def get_nome_classe(self):
        return self.nome_classe

    def jogar_carta(self, alvo):
        print(f"{alvo.get_nome()} equipou {self.nome_classe}")
        alvo.equipar_classe(self)

