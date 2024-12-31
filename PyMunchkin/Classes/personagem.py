class Personagem:
    def __init__(self):
        self.nivel = 1
        self.raca = None
        self.classe = None
        self.inventario = None
        self.maldicoesAtivas = None
        self.forcaCombate = self.calcular_forca_combate()

    # Gets
    def get_nivel(self):
        return self.nivel

    def get_raca(self):
        return self.raca

    def get_classe(self):
        return self.classe

    def get_forca_combate(self):
        return self.forcaCombate

        # stats["Raca"] = self.personagem.getRaca()
        # stats["Classe"] = self.personagem.getClasse()
        # stats["Forca"] = self.personagem.getForcaCombate()

    # Sets/Alter
    def equipar_raca(self, raca):
        self.raca = raca

    def equipar_classe(self, classe):
        self.classe = classe

    def mudar_forca_combate(self, quantidade):
        self.forcaCombate += quantidade

    def adiciona_ao_nivel(self, quantidade):
        if self.nivel == 10 and quantidade > 0:
            return
        if self.nivel == 1 and quantidade < 0:
            return
        self.nivel += quantidade

    # Combate
    def calcular_forca_combate(self):
        return self.nivel
