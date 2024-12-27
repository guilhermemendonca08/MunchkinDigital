class Personagem:
    def __init__(self, nivel, maldicoesAtivas, inventario):
        self.nivel = nivel
        self.raca = None
        self.classe = None
        self.inventario = inventario
        self.maldicoesAtivas = None
        self.forcaCombate = self.calcularForcaCombate()

    def mudarNivel(self, quantidade):
        self.nivel += quantidade

    def calcularForcaCombate(self):
        return self.nivel

