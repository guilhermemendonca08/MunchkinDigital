from Classes.subject import Subject
from Classes.observer import Observer
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
from Classes.gerenciador_combate import GerenciadorCombate
from Classes.carta_item import Item
from Classes.carta_classe import Classe
from Classes.carta_raca import Raca
from Classes.carta_monstro import Monstro
from Classes.card_stack import CardStack
from Classes.lista_circular import ListaCircular
from Classes.ui_handler import UIHandler


class ControladorJogo(Subject):
    def __init__(self, janela):
        self.jogadores = ListaCircular()
        self.observers = []
        self.gerenciador_combate = GerenciadorCombate()
        self.add_observer(self.gerenciador_combate)
        self.deck_dungeon = CardStack("Assets/Door/000 (small).png")
        self.deck_dungeon_discard = CardStack("Assets/Door/000 (small)darkmode.png")
        self.deck_tesouro = CardStack("Assets/Treasure/100 (small).png")
        self.deck_tesouro_discard = CardStack("Assets/Treasure/100 (small)darkmode.png")
        self.jogador_atual = None
        self.carta_em_jogo = None
        self.estado_do_jogo = Inicializacao()
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
        self.ui_handler = UIHandler(janela.get_mouse())
        self.pending_card = None
        self.choice_needed = False
        self.mouse_input = janela.get_mouse()
        self.janela = janela
        self.freeze = False
        self.sfx = None

    def set_sfx(self, hover, reject, select, deal):
        self.sfx = {"hover": hover, "reject": reject, "select": select, "deal": deal}

    def freeze_game(self):
        self.freeze = True

    def unfreeze_game(self):
        self.freeze = False

    def coloca_carta_em_jogo(self, carta):
        self.carta_em_jogo = carta

    def get_carta_em_jogo(self):
        return self.carta_em_jogo

    def play_sfx(self, sound):
        self.sfx[sound].play()

    # UI related stuff

    # Mouse related stuff
    def is_mouse_left_click_pressed(self):
        return self.ui_handler.is_mouse_left_click_pressed(self.freeze)
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
        return self.ui_handler.mouse_over_card(self.jogadores)

    def mouse_over_object(self, objeto):
        return self.ui_handler.mouse_over_object(objeto)

    def clicked(self, target):
        return self.ui_handler.clicked(target, self.freeze)

    # Game Logic Stuff
    def is_choice_needed(self):
        return self.choice_needed

    def get_target_choices(self):
        acceptable_targets = []
        # TODO: utilizar valor sentinela para evitar warning de variável None.
        acceptable_types = self.pending_card.get_target_type()
        for target_type in acceptable_types:
            if target_type == "jogador":
                for each in self.jogadores:
                    acceptable_targets.append(each)
            elif target_type == "combatentes":
                for each in self.gerenciador_combate.get_combatentes():
                    acceptable_targets.append(each)
            elif target_type == "self":
                acceptable_targets.append(self.jogador_atual)
            # elif target_type = "carry":
            # acceptable_targets.append(self.jogadorAtual.get_inventario())
        return acceptable_targets

    def detect_choice(self):
        return self.ui_handler.detect_choice(self.get_target_choices())

    def detect_cancel(self):
        return self.ui_handler.is_mouse_right_click_pressed()

    def cancel_choice(self):
        if self.choice_needed:
            self.play_sfx("reject")
            self.choice_needed = False
            self.freeze = False
            self.pending_card = None
        return

    def play_choice(self, choice):
        self.play_attempt(self.pending_card, target=choice)

    def play_attempt(self, carta, **kwargs):
        jogador = self.jogador_atual
        # TODO: utilizar valor sentinela para evitar warning de variável None.
        if jogador.has_card(carta):
            if self.estado_do_jogo.aceita_carta(carta):
                if (
                    carta.get_tipo() == "raca"
                    or carta.get_tipo() == "classe"
                    or (carta.get_tipo() == "item" and not carta.get_uso_unico())
                ):
                    self.play_sfx("select")
                    print(f"I play {carta.get_nome()}!")
                    self.jogador_atual.jogar_carta(carta, jogador)
                    # carta.jogar_carta(jogador)  # self cast
                    # TODO: utilizar valor sentinela para evitar warning de variável None.
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
                        self.play_sfx("select")
                        self.jogador_atual.jogar_carta(carta, kwargs.get("target"))
                        # carta.jogar_carta(kwargs.get("target"))
                        # TODO: utilizar valor sentinela para evitar warning de variável None.
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
        return self.deck_dungeon

    def get_deckTesouro(self):
        return self.deck_tesouro

    def discard_card(self, card):
        print(f"Carta descartada: {card.get_nome()}")
        if card.get_deckOrigem() == "dungeon":
            self.retornaAoDeck(self.deck_dungeon_discard, card)
            print(
                # f"Novo tamanho da pilha descarte: {self.deckDungeonDiscard.getSize()}"
            )
        elif card.get_deckOrigem() == "tesouro":
            self.retornaAoDeck(self.deck_tesouro_discard, card)
            print(
                # f"Novo tamanho da pilha descarte: {self.deckTesouroDiscard.getSize()}"
            )
        else:
            raise Exception("Carta sem deck de origem")

    # End of deck related stuff

    def proximoTurno(self):
        self.jogador_atual = self.jogadores.proximo()

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
            self.add_observer(jogador)
            jogador.set_discard_callback(self.discard_card)
            self.jogadores.adiciona(jogador)
        else:
            print("Número máximo de jogadores atingido")

    def set_jogadorAtual(self, jogador):
        self.jogador_atual = jogador

    def get_jogador_atual(self):
        if not self.jogador_atual:
            return None
        return self.jogador_atual

    # Gerenciamento de estados do jogo
    def iniciarJogo(self):
        pass

    def executarFase(self):
        self.estado_do_jogo.executa_fase(self)

    def proximoEstado(self, novoEstado):
        self.notify_observers(novoEstado)
        self.estado_do_jogo = self.estados[novoEstado]

    def get_estadoDoJogo(self):
        estadoDoJogo = self.estado_do_jogo.get_estado_do_jogo()
        return estadoDoJogo

    # Carregamento de cartas
    def carregaCartas(self, cards, pilha):
        for each in cards:
            pilha.push_wherever(each)
        pilha.shuffle()

    # SUBJECT/ OBSERVER PATTERN
    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
        pass

    def notify_observers(self, estado_do_jogo: str):
        for each in self.observers:
            each.update(estado_do_jogo)
