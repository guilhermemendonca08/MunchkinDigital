class Personagem:
    def __init__(self):
        self.nivel = 1
        self.raca = None
        self.classe = None
        self.inventario = None
        self.maldicoesAtivas = None
        self.forcaCombate = self.calcularForcaCombate()

    def mudarNivel(self, quantidade):
        self.nivel += quantidade

    def calcularForcaCombate(self):
        return self.nivel

