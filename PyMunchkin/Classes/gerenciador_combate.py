from Classes.estado import Estado
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

    def get_battle_situation(self):
        string = "Jogador: "
        string += str(self.jogador[0].calcular_forca_combate())
        string += " vs Monstro: "
        string += str(self.monstro[0].calcular_forca_combate())
        return string

    def get_forca_monstros(self):
        soma = 0
        for each in self.monstro:
            soma += each.calcular_forca_combate()
        # print(soma)
        return soma

    def get_forca_jogadores(self):
        soma = 0
        for each in self.jogador:
            soma += each.calcular_forca_combate()
        return soma

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
    def update(self, estado_do_jogo, jogador_atual, carta_em_jogo):
        if estado_do_jogo == "Combate":
            # print("beep, boop, gerenciador de combate diz:")
            # print("Jogador atual: ", jogador_atual.get_nome())
            # print("Monstro atual: ", carta_em_jogo.get_nome())
            self.jogador = [jogador_atual]
            self.jogador[0].reseta_buffs()
            self.monstro = [carta_em_jogo]
            self.monstro[0].reseta_buffs()
