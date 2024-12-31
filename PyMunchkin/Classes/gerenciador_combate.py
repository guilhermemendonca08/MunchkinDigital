from Classes.observer import Observer
from Classes.jogador import Jogador
from Classes.carta_monstro import Monstro


class GerenciadorCombate(Observer):

    def __init__(self):
        self.jogador = []
        self.monstro = []
        self.vantagens = {"jogador": 0, "monstro": 0}

    def resolverCombate(self):
        """
        Função que resolve o combate entre jogador e monstro
        :return: 1 se o jogador venceu, 0 se o monstro venceu
        """
        playerstr = 0
        monstrostr = 0
        for each in self.jogador:
            playerstr += each.jogador.calcularForca()

        for each in self.monstro:
            monstrostr += each.monstro.calcularForca()

        if playerstr > monstrostr:
            return 1
        else:
            return 0

    def calcularVantagens(self):
        pass

    def aplicarConsequencias(self, vitoria):
        pass

    def add_jogador(self, jogador):
        self.jogador.append(jogador)

    def add_monstro(self, monstro):
        self.monstro.append(monstro)

    def get_monstros(self):
        return self.monstro

    def get_combatentes(self):
        return self.jogador + self.monstro

    # SUBJECT/ OBSERVER PATTERN
    def update(self, estado_do_jogo: str):
        if estado_do_jogo == "Combate":
            print("MY TIME TO SHINE!!!!")
