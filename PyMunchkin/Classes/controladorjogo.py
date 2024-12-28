from Classes.estado_inicializacao import Inicializacao
from Classes.estado_aguardandojogada import AguardandoJogada
from Classes.estado_caridade import Caridade
from Classes.estado_chutarporta import ChutarPorta
from Classes.estado_combate import Combate
from Classes.estado_finalizado import Finalizado
from Classes.estado_fuga import Fuga
from Classes.estado_procurarencrenca import ProcurarEncrenca
from Classes.estado_saquear import Saquear
from Classes.gerenciadorcombate import GerenciadorCombate
from Classes.carta_item import Item
from Classes.carta_classe import Classe
from Classes.carta_raca import Raca
from Classes.cardstack import CardStack


class ControladorJogo:
    def __init__(self):
        self.jogadores = []
        self.observers = []
        self.deckDungeon = CardStack()
        self.deckTesouro = CardStack()
        self.jogadorAtual = None
        self.estadoDoJogo = Inicializacao()
        self.gerenciadorCombate = GerenciadorCombate()
        self.estados = {
            "AguardandoJogada": AguardandoJogada(),
            "Caridade": Caridade(),
            "ChutarPorta": ChutarPorta(),
            "Combate": Combate(),
            "Finalizado": Finalizado(),
            "Fuga": Fuga(),
            "ProcurarEncrenca": ProcurarEncrenca(),
            "Saquear": Saquear(),
        }

    # Deck related stuff
    # Adiciona uma carta ao topo deck
    def adicionaAoDeck(self, deck, carta):
        deck.push(carta)

    # Adiciona uma carta ao fundo do deck
    def retornaAoDeck(self, deck, carta):
        deck.push_bottom(carta)

    # Embaralha o deck
    def shuffleDeck(self, deck):
        deck.shuffle()

    # Remove uma carta do topo do deck e a retorna
    def comprarCarta(self, deck):
        return deck.pop()

    # End of deck related stuff

    def proximoTurno(self):
        pass

    def verificarVencedor(self):
        winners = []
        for each in self.jogadores:
            if each.get_character_level() >= 10:
                winners.append(each)
        return winners

    def finalizarJogo(self):
        pass

    def add_jogador(self, jogador):
        self.jogadores.append(jogador)

    def get_jogadorAtual(self):
        if not self.jogadorAtual:
            return "Nenhum jogador"
        return self.jogadorAtual

    # Gerenciamento de estados do jogo
    def iniciarJogo(self):
        pass

    def executarFase(self):
        self.estadoDoJogo.executaFase(self)

    def proximoEstado(self, novoEstado):
        self.estadoDoJogo = self.estados[novoEstado]

    def get_estadoDoJogo(self):
        estadoDoJogo = self.estadoDoJogo.get_EstadoDoJogo()
        return estadoDoJogo

    # Carregamento de cartas
    def carregaCartas(self):
        cartas_tesouro = [
            Item(
                "Assets/treasure/101 (small).png",
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
                "Assets/treasure/103 (small).png",
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
                "Assets/treasure/104 (small).png",
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
                "Assets/treasure/105 (small).png",
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
                "Assets/treasure/108 (small).png",
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
        for each in cartas_tesouro:
            self.deckTesouro.push_wherever(each)
        cartas_dungeon = [
            Raca(
                "Assets/Door/001 (small).png",
                "Elf",
                "You go up a level for every monster you help someone else kill",
                None,
                "raça",
                "Run Away",
            ),
            Raca(
                "Assets/Door/002 (small).png",
                "Elf",
                "You go up a level for every monster you help someone else kill",
                None,
                "raça",
                "Run Away",
            ),
            Raca(
                "Assets/Door/003 (small).png",
                "Elf",
                "You go up a level for every monster you help someone else kill",
                None,
                "raça",
                "Run Away",
            ),
            Raca(
                "Assets/Door/004 (small).png",
                "Halfling",
                "You may sell one item each turn for double price",
                None,
                "raça",
                "Discard Refresh",
            ),
            Raca(
                "Assets/Door/005 (small).png",
                "Halfling",
                "You may sell one item each turn for double price",
                None,
                "raça",
                "Discard Refresh",
            ),
            Raca(
                "Assets/Door/006 (small).png",
                "Halfling",
                "You may sell one item each turn for double price",
                None,
                "raça",
                "Discard Refresh",
            ),
            Raca(
                "Assets/Door/007 (small).png",
                "Dwarf",
                "You can carry any number of Big items",
                None,
                "raça",
                "Can have 6 items in hand",
            ),
            Raca(
                "Assets/Door/008 (small).png",
                "Dwarf",
                "You can carry any number of Big items",
                None,
                "raça",
                "Can have 6 items in hand",
            ),
            Raca(
                "Assets/Door/009 (small).png",
                "Dwarf",
                "You can carry any number of Big items",
                None,
                "raça",
                "Can have 6 items in hand",
            ),
            Classe(
                "Assets/Door/016 (small).png",
                "Warrior",
                "Berskerking: You may discard up to 3 cardss in combat; each one gives you +1 bonus",
                None,
                "classe",
                "Wins ties in combat",
            ),
            Classe(
                "Assets/Door/017 (small).png",
                "Warrior",
                "Berskerking: You may discard up to 3 cardss in combat; each one gives you +1 bonus",
                None,
                "classe",
                "Wins ties in combat",
            ),
            Classe(
                "Assets/Door/018 (small).png",
                "Warrior",
                "Berskerking: You may discard up to 3 cardss in combat; each one gives you +1 bonus",
                None,
                "classe",
                "Wins ties in combat",
            ),
            Classe(
                "Assets/Door/019 (small).png",
                "Wizard",
                "Harry, you're a wizard.",
                None,
                "classe",
                "Flight Spell",
            ),
            Classe(
                "Assets/Door/020 (small).png",
                "Wizard",
                "Harry, you're a wizard.",
                None,
                "classe",
                "Flight Spell",
            ),
            Classe(
                "Assets/Door/021 (small).png",
                "Wizard",
                "Harry, you're a wizard.",
                None,
                "classe",
                "Flight Spell",
            ),
        ]
        for each in cartas_dungeon:
            self.deckDungeon.push_wherever(each)
