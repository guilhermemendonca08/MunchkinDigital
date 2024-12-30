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

    def colocaCartaEmJogo(self, carta):
        self.cartaEmJogo = carta

    def get_cartaEmJogo(self):
        return self.cartaEmJogo

    def mouse_over_card(self):
        return self.uihandler.mouse_over_card(self.jogadores)

    def mouse_over_object(self, objeto):
        return self.uihandler.mouse_over_object(objeto)

    def aceita_carta(self, carta):
        return self.estadoDoJogo.aceita_carta(carta)

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

    def get_deckDungeon(self):
        return self.deckDungeon

    def get_deckTesouro(self):
        return self.deckTesouro

    def discard_card(self, card):
        print(f"Carta descartada: {card.get_nome()}")
        if card.get_deckOrigem() == "dungeon":
            self.retornaAoDeck(self.deckDungeonDiscard, card)
            print(
                # f"Novo tamanho da pilha descarte: {self.deckDungeonDiscard.getSize()}"
            )
        elif card.get_deckOrigem() == "tesouro":
            self.retornaAoDeck(self.deckTesouroDiscard, card)
            print(
                # f"Novo tamanho da pilha descarte: {self.deckTesouroDiscard.getSize()}"
            )
        else:
            raise Exception("Carta sem deck de origem")

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
            jogador.set_discard_callback(self.discard_card)
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
    def carregaCartas(self, cards, pilha):
        for each in cards:
            pilha.push_wherever(each)
