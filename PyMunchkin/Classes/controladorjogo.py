from PPlay.window import mouse
from PPlay.sound import Sound
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
        self.pending_card = None
        self.choice_needed = False
        self.mouse_input = janela.get_mouse()
        self.janela = janela
        self.freeze = False

    def Set_SFX(self, hover, reject, select, deal):
        self.SFX = {"hover": hover, "reject": reject, "select": select, "deal": deal}

    def freeze_game(self):
        self.freeze = True

    def unfreeze_game(self):
        self.freeze = False

    def colocaCartaEmJogo(self, carta):
        self.cartaEmJogo = carta

    def get_cartaEmJogo(self):
        return self.cartaEmJogo

    def play_SFX(self, sound):
        self.SFX[sound].play()

    # UI related stuff

    # Mouse related stuff
    def is_mouse_left_click_pressed(self):
        return self.uihandler.is_mouse_left_click_pressed(self.freeze)
        # if self.freeze is False:
        #     return self.mouse_input.is_button_pressed(1)
        # else:
        #     return False

    def is_mouse_right_click_pressed(self):
        if self.freeze is False:
            return self.mouse_input.is_button_pressed(3)
        else:
            return False

    def mouse_over_card(self):
        return self.uihandler.mouse_over_card(self.jogadores)

    def mouse_over_object(self, objeto):
        return self.uihandler.mouse_over_object(objeto)

    def clicked(self, target):
        return self.uihandler.clicked(target, self.freeze)

    # Game Logic Stuff
    def is_choice_needed(self):
        return self.choice_needed

    def get_target_choices(self):
        acceptable_targets = []
        acceptable_types = self.pending_card.get_target_type()
        for target_type in acceptable_types:
            if target_type == "jogador":
                for each in self.jogadores:
                    acceptable_targets.append(each)
            elif target_type == "monstro":
                for each in self.gerenciadorCombate.get_monstros():
                    acceptable_targets.append(each)
            elif target_type == "self":
                acceptable_targets.append(self.jogadorAtual)
            # elif target_type = "carry":
            # acceptable_targets.append(self.jogadorAtual.get_inventario())
        return acceptable_targets

    def detect_choice(self):
        return self.uihandler.detect_choice(self.get_target_choices())

    def play_choice(self, choice):
        self.play_attempt(self.pending_card, target=choice)

    def play_attempt(self, carta, **kwargs):
        jogador = self.jogadorAtual
        if jogador.has_card(carta):
            if self.estadoDoJogo.aceita_carta(carta):
                if (
                    carta.get_tipo() == "raca"
                    or carta.get_tipo() == "classe"
                    or (carta.get_tipo() == "item" and not carta.get_usoUnico())
                ):
                    self.play_SFX("select")
                    print(f"I play {carta.get_nome()}!")
                    carta.jogarCarta(jogador)  # self cast
                    jogador.remove_card(carta)
                else:
                    if kwargs.get("target") is None:
                        self.pending_card = carta
                        self.choice_needed = True
                        self.freeze = True
                    else:
                        self.freeze = False
                        self.choice_needed = False
                        self.pending_card = None
                        self.play_SFX("select")
                        carta.jogarCarta(kwargs.get("target"))
                        jogador.remove_card(carta)
            else:
                # self.play_SFX("reject")
                print("Carta não pode ser jogada")
        else:
            print(f"{carta.get_descricao()}")

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
        pilha.shuffle()
