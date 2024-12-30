class Personagem:
    def __init__(self):
        self.nivel = 1
        self.raca = None
        self.classe = None
        self.inventario = None
        self.maldicoesAtivas = None
        self.forcaCombate = self.calcularForcaCombate()

    def getNivel(self):
        return self.nivel

    def mudarForcaCombate(self, quantidade):
        self.forcaCombate += quantidade

    def adicionaAoNivel(self, quantidade):
        if self.nivel == 10 and quantidade > 0:
            return
        if self.nivel == 1 and quantidade < 0:
            return
        self.nivel += quantidade

    def calcularForcaCombate(self):
        return self.nivel
