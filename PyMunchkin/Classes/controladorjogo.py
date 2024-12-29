from PPlay.window import mouse
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
from Classes.carta_monstro import Monstro
from Classes.cardstack import CardStack
from Classes.listacircular import ListaCircular
from Classes.ui_handler import UIHandler


class ControladorJogo:
    # def __init__(self, mouse_input):
    def __init__(self, janela):
        self.jogadores = ListaCircular()
        self.observers = []
        self.deckDungeon = CardStack("Assets/Door/000 (small).png")
        self.deckDungeonDiscard = CardStack("Assets/Door/000 (small)darkmode.png")
        self.deckTesouro = CardStack("Assets/Treasure/100 (small).png")
        self.deckTesouroDiscard = CardStack("Assets/Treasure/100 (small)darkmode.png")
        self.jogadorAtual = None
        self.cartaEmJogo = None
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
        self.uihandler = UIHandler(janela.get_mouse())
        self.mouse_input = janela.get_mouse()
        self.janela = janela

    # def set_uihandler(self, uihandler):
    #     self.uihandler = UIHandler(mouse)
    def colocaCartaEmJogo(self, carta):
        self.cartaEmJogo = carta

    def get_cartaEmJogo(self):
        return self.cartaEmJogo

    def mouse_over_card(self):
        return self.uihandler.mouse_over_card(self.jogadores)

    def mouse_over_object(self, objeto):
        return self.uihandler.mouse_over_object(objeto)

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
        self.jogadorAtual = self.jogadores.proximo()

    def verificarVencedor(self):
        winners = []
        for each in self.jogadores:
            if each.get_character_level() >= 10:
                winners.append(each)
        return winners

    def finalizarJogo(self):
        pass

    def add_jogador(self, jogador):
        if self.jogadores.get_size() < 4:
            self.jogadores.adiciona(jogador)
        else:
            print("Número máximo de jogadores atingido")

    def set_jogadorAtual(self, jogador):
        self.jogadorAtual = jogador

    def get_jogadorAtual(self):
        if not self.jogadorAtual:
            return None
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
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/102 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/103 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/105 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
            ),
            Item(
                "Assets/treasure/101 (small).png",
                "Magic Missile",
                "Use during combat. +5 to either side. Usable only once",
                "buff",
                "item",
                "tesouro",
                None,
                None,
                300,
                None,
                True,
                None,
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
            Monstro(
                "Assets/Door/061 (small).png",
                "Maul Rat",
                "A creature from Hell. +3 against Clerics.",
                None,  # efeito
                "monstro",  # tipo
                1,  # nivel
                1,  # qntTesouro
                "level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/062 (small).png",
                "Lame Goblin",
                "+1 to run away",
                None,  # efeito
                "monstro",  # tipo
                1,  # nivel
                1,  # qntTesouro
                "level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/064 (small).png",
                "Flying Frogs",
                "-1 to run away",
                None,  # efeito
                "monstro",  # tipo
                2,  # nivel
                1,  # qntTesouro
                "2x level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/065 (small).png",
                "Gelatinous Octahedron",
                "+1 to run away",
                None,  # efeito
                "monstro",  # tipo
                2,  # nivel
                1,  # qntTesouro
                "Drop all big items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/066 (small).png",
                "Mr. Bones",
                "If you must flee, you lose a level even when you escape.",
                None,  # efeito
                "monstro",  # tipo
                2,  # nivel
                1,  # qntTesouro
                "2x level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/067 (small).png",
                "Large Angry Chicken",
                "Fried Chicken is delicious. Gain an extra level if you kill it with fire or flame.",
                None,  # efeito
                "monstro",  # tipo
                2,  # nivel
                1,  # qntTesouro
                "level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/068 (small).png",
                "Pit Bull",
                "If you can't defeat it, you may escape by dropping any wand, pole or staff",
                None,  # efeito
                "monstro",  # tipo
                2,  # nivel
                1,  # qntTesouro
                "2x level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/069 (small).png",
                "Leperchaun",
                "He's gross! +5 against elves",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 2 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/070 (small).png",
                "Undead Horse",
                "+5 against dwarves",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "2x level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/071 (small).png",
                "Harpies",
                "+5 against wizards",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "2x level down",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),  # repeats after this point
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
            Monstro(
                "Assets/Door/072 (small).png",
                "Snails on speed",
                "-2 to Run Away",
                None,  # efeito
                "monstro",  # tipo
                4,  # nivel
                2,  # qntTesouro
                "Lose 1-6 items",  # coisaRuim
            ),
        ]
        for each in cartas_dungeon:
            self.deckDungeon.push_wherever(each)
