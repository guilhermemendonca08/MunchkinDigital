from Classes.estado_inicializacao import Inicializacao
from Classes.gerenciadorcombate import GerenciadorCombate
from Classes.carta import Carta
from Classes.carta_item import Item


class ControladorJogo:
    def __init__(self):
        self.jogadores = []
        self.observers = []
        self.deckDungeon = None
        self.deckTesouro = []
        self.jogadorAtual = None
        self.estadoDoJogo = Inicializacao()
        self.gerenciadorCombate = GerenciadorCombate()

    def carregaCartas(self):
        self.deckTesouro = [
            Item(
                "Assets/treasure/101.png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                0,
                0,
                300,
                None,
                True,
            ),
            Item(
                "Assets/treasure/103.png",
                "Potion of Halitosis",
                "Use during combat. +2 to either side, or instantly kills the floating nose. Usable only once",
                "buff",
                "item",
                0,
                0,
                100,
                None,
                True,
            ),
            Item(
                "Assets/treasure/104.png",
                "Swiss Army Polearm",
                "Usable by Human Only",
                "weapon",
                "item",
                4,
                2,
                600,
                "Human",
                False,
            ),
            Item(
                "Assets/treasure/105.png",
                "Buckler of Swashing",
                " ",
                "shield",
                "item",
                2,
                1,
                400,
                None,
                False,
            ),
            Item(
                "Assets/treasure/108.png",
                "Slimy Armor",
                " ",
                "armor",
                "item",
                1,
                0,
                200,
                None,
                False,
            ),
        ]

    def iniciarJogo(self):
        pass

    def proximoTurno(self):
        pass

    def executarFase(self):
        self.estadoDoJogo.executaFase(self)
        pass

    def comprarCarta(self):
        pass

    def verificarVencedor(self):
        winners = []
        for each in self.jogadores:
            if each.get_character_level() >= 10:
                winners.append(each)
        return winners

    def finalizarJogo(self):
        pass

    # Getters
    def get_jogadorAtual(self):
        if not self.jogadorAtual:
            return "Nenhum jogador"
        return self.jogadorAtual

    def get_estadoDoJogo(self):
        faseDoJogo = self.estadoDoJogo.get_faseDoJogo()
        return faseDoJogo

    def add_jogador(self, jogador):
        self.jogadores.append(jogador)

