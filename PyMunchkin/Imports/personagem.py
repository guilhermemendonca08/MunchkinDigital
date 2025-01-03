from math import copysign


class Personagem:
    def __init__(self):
        self.nivel = 1
        self.raca = None
        self.classe = None
        self.inventario = None
        self.maldicoesAtivas = None
        self.bonus_combate = 0
        self.forcaCombate = self.calcular_forca_combate()

    def aplicar_buff(self, valor):
        self.bonus_combate += valor

    # Gets
    # def morrer(self):
    #     # perde todos os itens equipados.
    #     return

    def get_nivel(self):
        return self.nivel

    def get_raca(self):
        return self.raca

    def get_classe(self):
        return self.classe

    def get_forca_combate(self):
        return self.forcaCombate

    def reseta_buffs(self):
        self.bonus_combate = 0

    # Sets/Alter
    def equipar_raca(self, raca):
        self.raca = raca

    def equipar_classe(self, classe):
        self.classe = classe

    def mudar_forca_combate(self, quantidade):
        self.forcaCombate += quantidade

    def adiciona_ao_nivel(self, quantidade):
        for _ in range(abs(quantidade)):
            if self.nivel == 1 and quantidade < 0:
                return
            if self.nivel == 10 and quantidade > 0:
                return
            self.nivel += int(copysign(1, quantidade))
            print(f"nivel é : {self.nivel}, adição de {quantidade}")
            # if self.nivel == 10 or self.nivel == 1:
            #     return

    # Combate
    def calcular_forca_combate(self):
        somatorio = 0
        somatorio += self.nivel
        somatorio += self.bonus_combate
        return somatorio
