from Classes.carta import Carta


class Monstro(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        deck_origem,
        nivel,
        qnt_tesouro,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo, deck_origem)
        self.nivel = nivel
        self.qntTesouro = qnt_tesouro
        self.bonus_combate = 0
    
    def calcular_forca_combate(self):
        return self.nivel + self.bonus_combate
