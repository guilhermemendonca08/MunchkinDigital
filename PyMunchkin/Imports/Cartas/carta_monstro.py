from Imports.Cartas.carta import Carta
from Imports.targetable import Targetable


class Monstro(Carta, Targetable):
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
        self.qnt_tesouro = qnt_tesouro
        self.bonus_combate = 0

    def get_qnt_tesouro(self):
        return self.qnt_tesouro

    def calcular_forca_combate(self):
        return self.nivel + self.bonus_combate

    def aplicar_buff(self, valor):
        self.bonus_combate += valor

    def reseta_buffs(self):
        self.bonus_combate = 0

    def get_target_type(self):
        pass

    def aplica_bad_stuff(self, jogador):
        self.executar_efeito(jogador)

    def executar_efeito(self, alvo):
        self.efeito.aplicar_efeito(alvo)

