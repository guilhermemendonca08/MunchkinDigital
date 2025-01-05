from Imports.subject import Subject
from Imports.observer import Observer
from Imports.Estados.estado_inicializacao import Inicializacao
from Imports.Estados.estado_aguardandojogada import AguardandoJogada
from Imports.Estados.estado_caridade import Caridade
from Imports.Estados.estado_chutarporta import ChutarPorta
from Imports.Estados.estado_combate import Combate
from Imports.Estados.estado_finalizado import Finalizado
from Imports.Estados.estado_fuga import Fuga
from Imports.Estados.estado_procurarencrenca import ProcurarEncrenca
from Imports.Estados.estado_saquear import Saquear
from Imports.gerenciador_combate import GerenciadorCombate
from Imports.Utils.card_stack import CardStack
from Imports.Utils.lista_circular import ListaCircular
from Imports.ui_handler import UIHandler


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
        self.jogador_ativo = None
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
        self.ui_handler = UIHandler(janela)
        self.pending_card = None
        self.choice_needed = False
        self.mouse_input = janela.get_mouse()
        self.janela = janela
        self.freeze = False
        self.sfx = None

    def get_card_description(self):
        return self.ui_handler.get_card_description(self.jogadores)

    def revive_jogador(self, jogador):
        jogador.revive()

    def get_lista_jogadores(self):
        return self.jogadores.exporta_lista()

    def proximo_depois_de(self, jogador):
        return self.jogadores.proximo_depois_de(jogador)

    def level_up(self, jogador):
        jogador.level_up()

    def jogador_compra_carta(self, jogador, deck):
        carta = self.comprar_carta(deck)
        jogador.add_card(carta)
        return carta

    def get_resultado_combate(self):
        return self.gerenciador_combate.resolver_combate()

    def finaliza_combate(self):
        self.gerenciador_combate.finaliza_combate()

    def get_battle_situation(self):
        return self.gerenciador_combate.get_battle_situation()

    def set_sfx(self, hover, reject, select, deal):
        self.sfx = {"hover": hover, "reject": reject, "select": select, "deal": deal}

    def freeze_game(self):
        self.freeze = True

    def unfreeze_game(self):
        self.freeze = False

    def coloca_carta_em_jogo(self, carta):
        self.carta_em_jogo = carta

    def remove_carta_em_jogo(self):
        self.carta_em_jogo = None

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
            elif target_type == "monstro":
                for each in self.gerenciador_combate.get_monstros():
                    acceptable_targets.append(each)
            elif target_type == "self":
                acceptable_targets.append(self.jogador_ativo)
            # elif target_type = "carry":
            # acceptable_targets.append(self.jogadorAtual.get_inventario())
        return acceptable_targets

    # Needs a target_list, gets it from self.get_target_choices()
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

    def is_their_turn(self):
        return self.jogador_ativo == self.jogador_atual

    # Detecta com alvo [alvo]
    def detect_exact_choice(self, target):
        return self.ui_handler.detect_choice(target)

    def play_attempt(self, carta, **kwargs):
        jogador = self.jogador_ativo
        # TODO: utilizar valor sentinela para evitar warning de variável None.
        if jogador.has_card(carta):
            if self.estado_do_jogo.aceita_carta(carta):
                # Cartas de uso "instantâneo"
                if carta.get_tipo() in {"raca", "classe", "equipamento"}:
                    self.play_sfx("select")
                    print(f"I play {carta.get_nome()}!")
                    self.jogador_ativo.jogar_carta(carta, jogador)
                    # TODO: utilizar valor sentinela para evitar warning de variável None.
                    jogador.remove_card(carta)
                # Cartas que necessitam de alvo
                elif carta.get_tipo() == "monstro":
                    if self.is_their_turn():
                        self.coloca_carta_em_jogo(carta)
                        self.jogador_ativo.remove_card(carta)
                        self.proximo_estado("Combate")
                    else:
                        print(f"{carta.get_descricao()}")
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
                        self.jogador_ativo.jogar_carta(carta, kwargs.get("target"))
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
    def adiciona_ao_deck(self, deck, carta):
        deck.push(carta)

    # Adiciona uma carta ao fundo do deck
    def retorna_ao_deck(self, deck, carta):
        deck.push_bottom(carta)

    # Embaralha o deck
    def shuffle_deck(self, deck):
        deck.shuffle()

    # Remove uma carta do topo do deck e a retorna
    def comprar_carta(self, deck):
        if deck.get_size() == 0:
            if deck == self.deck_dungeon:
                self.recarrega_deck(self.deck_dungeon, self.deck_dungeon_discard)
            elif deck == self.deck_tesouro:
                self.recarrega_deck(self.deck_tesouro, self.deck_tesouro_discard)
            else:
                raise Exception("Deck de descarte associado não encontrado")
        return deck.pop()

    def recarrega_deck(self, deck, deck_discard):
        while deck_discard.get_size() > 0:
            carta = deck_discard.pop()
            deck.push(carta)
        deck.shuffle()

    def get_deck_dungeon(self):
        return self.deck_dungeon

    def get_deck_tesouro(self):
        return self.deck_tesouro

    def discard_card(self, card):
        print(f"Carta descartada: {card.get_nome()}")
        if card.get_deckOrigem() == "dungeon":
            self.retorna_ao_deck(self.deck_dungeon_discard, card)
            print(
                # f"Novo tamanho da pilha descarte: {self.deckDungeonDiscard.getSize()}"
            )
        elif card.get_deckOrigem() == "tesouro":
            self.retorna_ao_deck(self.deck_tesouro_discard, card)
            print(
                # f"Novo tamanho da pilha descarte: {self.deckTesouroDiscard.getSize()}"
            )
        else:
            raise Exception("Carta sem deck de origem")

    # End of deck related stuff

    def proximo_turno(self):
        self.jogador_ativo = self.jogadores.proximo()

    def verificar_vencedor(self):
        winners = []
        for each in self.jogadores:
            if each.get_character_level() >= 10:
                winners.append(each)
        return winners

    def finalizar_jogo(self):
        pass

    def add_jogador(self, jogador):
        if self.jogadores.get_size() < 4:
            self.add_observer(jogador)
            jogador.set_discard_callback(self.discard_card)
            self.jogadores.adiciona(jogador)
        else:
            print("Número máximo de jogadores atingido")

    def set_jogador_ativo(self, jogador):
        self.jogador_ativo = jogador

    def set_jogador_atual(self, jogador):
        self.jogador_atual = jogador

    def get_jogador_ativo(self):
        if not self.jogador_ativo:
            return None
        return self.jogador_ativo

    def get_jogador_atual(self):
        if not self.jogador_atual:
            return None
        return self.jogador_atual

    # Gerenciamento de estados do jogo
    def iniciar_jogo(self):
        pass

    def executar_fase(self):
        self.estado_do_jogo.executa_fase(self)

    def proximo_estado(self, novoEstado):
        self.notify_observers(novoEstado, self.jogador_ativo, self.carta_em_jogo)
        self.estado_do_jogo.reset()
        self.estado_do_jogo = self.estados[novoEstado]

    def get_estado_do_jogo(self):
        estadoDoJogo = self.estado_do_jogo.get_estado_do_jogo()
        return estadoDoJogo

    # Carregamento de cartas
    def carrega_cartas(self, cards, pilha):
        for each in cards:
            pilha.push_wherever(each)
        pilha.shuffle()

    # SUBJECT/ OBSERVER PATTERN
    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, estado_do_jogo, jogador_ativo, carta_em_jogo):
        for each in self.observers:
            each.update(estado_do_jogo, jogador_ativo, carta_em_jogo)

    # Debug stuff
    def load_card_by_name_in_deck(self, card_name):
        carta = self.busca_carta_por_nome(card_name)
        if carta is None:
            print("Carta não encontrada")
            return False
        if carta.get_deckOrigem() == "dungeon":
            self.deck_dungeon.push(carta)
        elif carta.get_deckOrigem() == "tesouro":
            self.deck_tesouro.push(carta)
        else:
            print("Carta não possui deck de origem")
            return False
        return True

    def busca_carta_por_nome(self, nome):
        for each in self.deck_dungeon:
            if each.get_nome() == nome:
                return each
        for each in self.deck_tesouro:
            if each.get_nome() == nome:
                return each
        return None
