class Personagem:
    def __init__(self):
        self.nivel = 1
        self.raca = None
        self.classe = None
        self.inventario = None
        self.maldicoesAtivas = None
        self.forcaCombate = self.calcularForcaCombate()

    # Gets
    def getNivel(self):
        return self.nivel

    def getRaca(self):
        return self.raca

    def getClasse(self):
        return self.classe

    def getForcaCombate(self):
        return self.forcaCombate

        # stats["Raca"] = self.personagem.getRaca()
        # stats["Classe"] = self.personagem.getClasse()
        # stats["Forca"] = self.personagem.getForcaCombate()

    # Sets/Alter
    def equiparRaca(self, raca):
        self.raca = raca

    def equiparClasse(self, classe):
        self.classe = classe

    def mudarForcaCombate(self, quantidade):
        self.forcaCombate += quantidade

    def adicionaAoNivel(self, quantidade):
        if self.nivel == 10 and quantidade > 0:
            return
        if self.nivel == 1 and quantidade < 0:
            return

    # Combate
    def calcularForcaCombate(self):
        return self.nivel
