import json
import io
from constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
    DOOR_HURTBOX_OFFSET_X,
    DOOR_HURTBOX_OFFSET_Y,
    TREASURE_JSON_DATA,
    DUNGEON_JSON_DATA,
)
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.sound import Sound
from Classes.jogador import Jogador
from Classes.controlador_jogo import ControladorJogo

# from Classes.ui_handler import UIHandler
from Classes.card_factory import CardFactory

# from constants import CARD_WIDTH, CARD_HEIGHT
# from Classes.carta_item import Item

# Inicialização da janela e objetos básicos.
janela = Window(RES_WIDTH, RES_HEIGHT)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

# Debug Hotkeys
hotkey_1 = False  # passa turno pra outro jogador
hotkey_2 = False  # +1 level
hotkey_3 = False
hotkey_4 = False

# Input default
# mouse_click = False

# Assets Básicos
# GameImages estáticos.
fundo = GameImage("Assets/TableAssets/MarbleBlack.jpg")
choicefliter = GameImage("Assets/TableAssets/choice.png")
borda = GameImage("Assets/TableAssets/Border_Gray50.png")
borda.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
displaynivel = Sprite("Assets/Niveis/leveldisplay.png", 10)
msg_selecione_alvo = GameImage("Assets/TableAssets/select_target2.png")

# SFX
hover = Sound("Assets/SFX/STS_SFX_CardHover3_v1.ogg")
reject = Sound("Assets/SFX/SOTE_SFX_CardReject_v1.ogg")
select = Sound("Assets/SFX/SOTE_SFX_CardSelect_v2.ogg")
deal = Sound("Assets/SFX/STS_SFX_CardDeal8_v1.ogg")

# Elementos de controle do jogo.
controlador_jogo = ControladorJogo(janela)

# Carregamento de cartas
card_factory = CardFactory()
# Carrega cartas Tesouro
treasure_json_file = io.StringIO(TREASURE_JSON_DATA)  # Simula abertura do json
treasure_card_data = json.load(treasure_json_file)  # De json -> dict
treasure_cards = card_factory.carrega_cartas(treasure_card_data)  # dict -> lista
controlador_jogo.carregaCartas(treasure_cards, controlador_jogo.get_deckTesouro())

# Carrega cartas Dungeon
dungeon_json_file = io.StringIO(DUNGEON_JSON_DATA)
dungeon_card_data = json.load(dungeon_json_file)
dungeon_cards = card_factory.carrega_cartas(dungeon_card_data)
controlador_jogo.carregaCartas(dungeon_cards, controlador_jogo.get_deckDungeon())

# Carrega sons
controlador_jogo.set_sfx(hover, reject, select, deal)

# Inicia Jogadores
jogador1 = Jogador("Apollo", "Assets/Portraits/Archer.png")
jogador2 = Jogador("Freya", "Assets/Portraits/HumanF4.png")
jogador3 = Jogador("Antares", "Assets/Portraits/HumanM4.png")
jogador4 = Jogador("Raphael", "Assets/Portraits/FiendM1.png")

# Variaveis de apoio.
time_acc = 0

controlador_jogo.add_jogador(jogador1)
controlador_jogo.add_jogador(jogador2)
controlador_jogo.add_jogador(jogador3)
controlador_jogo.add_jogador(jogador4)
# controladorJogo.executarFase()
while True:
    dt = janela.delta_time()
    time_acc += dt
    controlador_jogo.ui_handler.right_clicked()

    # Eventos
    card_hovered = controlador_jogo.mouse_over_card()
    if controlador_jogo.clicked(card_hovered):
        controlador_jogo.play_attempt(card_hovered)

    if controlador_jogo.is_choice_needed():
        choice = controlador_jogo.detect_choice()
        controlador_jogo.play_choice(choice)
        if controlador_jogo.detect_cancel():
            controlador_jogo.cancel_choice()

    # Debugging Events
    # Muda de quem é a vez.
    if teclado.key_pressed("1") and not hotkey_1:
        hotkey_1 = True
        controlador_jogo.proximoTurno()
    if not teclado.key_pressed("1"):
        hotkey_1 = False

    # Muda o nivel do personagem
    if teclado.key_pressed("2") and not hotkey_2:
        hotkey_2 = True
        controlador_jogo.get_jogadorAtual().adiciona_ao_nivel_personagem(1)

    if not teclado.key_pressed("2"):
        hotkey_2 = False

    # Draws
    # Background, everything else should be placed AFTER this.
    fundo.draw()
    borda.draw()

    # Draw Players' Avatars
    avatar_offset_x = 0
    for each in controlador_jogo.jogadores:
        if each == controlador_jogo.get_jogadorAtual():
            each.avatar.set_position(0, RES_HEIGHT - each.get_avatar_y())
            each.draw()
        else:
            each.avatar.set_position(0 + avatar_offset_x, 0)
            avatar_offset_x += RES_WIDTH / 3
            each.scaled_draw(100, 100)

    # Draw Players' Hands
    avatar_offset_x = 0
    for each in controlador_jogo.jogadores:
        if each == controlador_jogo.get_jogadorAtual():
            each.draw_mao(RES_WIDTH / 2, RES_HEIGHT - CARD_HEIGHT)
        else:
            each.scaled_draw_mao(0 + avatar_offset_x, 100, 80, 124)
            avatar_offset_x += RES_WIDTH / 3

    # Draw Player's level
    avatar_offset_x = 0
    for each in controlador_jogo.jogadores:
        if each == controlador_jogo.get_jogadorAtual():
            displaynivel.set_position(each.get_avatar_x(), RES_HEIGHT - 100)
            displaynivel.set_curr_frame(each.get_nivel_personagem() - 1)
            displaynivel.draw()
        else:
            displaynivel.set_position(100 + avatar_offset_x, 0)
            displaynivel.set_curr_frame(each.get_nivel_personagem() - 1)
            displaynivel.draw()
            avatar_offset_x += RES_WIDTH / 3

    # Draw Player Stats
    player_stats_string = ""

    if controlador_jogo.get_jogadorAtual() is None:
        player_stats_dict = {"No player present": "No player present"}
    else:
        player_stats_dict = controlador_jogo.get_jogadorAtual().get_stats()

    stats_height_offset = 0
    for key, value in player_stats_dict.items():
        player_stats_string = f"{key}: {value}"
        janela.draw_text(
            player_stats_string,
            250,
            RES_HEIGHT - 200 + stats_height_offset,
            size=25,
            color=(255, 255, 0),
        )
        stats_height_offset += 30

    # Draw Card Stacks
    # Door Pile
    controlador_jogo.deck_dungeon.set_position(
        RES_WIDTH - 2.5 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controlador_jogo.deck_dungeon.draw()

    # Door Discard Pile
    controlador_jogo.deck_dungeon_discard.set_position(
        RES_WIDTH - 1.25 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controlador_jogo.deck_dungeon_discard.draw()

    # Treasure Pile
    controlador_jogo.deck_tesouro.set_position(
        0.25 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controlador_jogo.deck_tesouro.draw()

    # Treasure Discard Pile
    controlador_jogo.deck_tesouro_discard.set_position(
        1.5 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controlador_jogo.deck_tesouro_discard.draw()

    # Game Logic / Draws from phases
    controlador_jogo.executarFase()

    # Debugging Text
    # Jogador da vez e Fase do turno
    jogadoratual = controlador_jogo.get_jogadorAtual()
    if jogadoratual:
        player_turn_debug_text = jogadoratual.get_nome()
        player_turn_debug_text += "'s turn"
    else:
        player_turn_debug_text = "Nenhum jogador presente"
    phase_debug_text = controlador_jogo.get_estadoDoJogo()
    janela.draw_text(
        player_turn_debug_text,
        RES_WIDTH - 14 * len(player_turn_debug_text),
        RES_HEIGHT - 60,
        size=25,
        color=(255, 255, 0),
    )
    janela.draw_text(
        phase_debug_text,
        RES_WIDTH - 12 * len(phase_debug_text),
        RES_HEIGHT - 30,
        size=25,
        color=(255, 255, 0),
    )

    # Número de cartas nas pilhas.
    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_dungeon.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        10,
        RES_HEIGHT * 0.35,
        size=25,
        color=(255, 255, 0),
    )

    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_dungeon_discard.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        240,
        RES_HEIGHT * 0.62,
        size=25,
        color=(255, 255, 0),
    )

    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_tesouro.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        RES_WIDTH * 25 / 32,
        RES_HEIGHT * 0.35,
        size=25,
        color=(255, 255, 0),
    )

    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_tesouro_discard.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        1700,
        RES_HEIGHT * 0.62,
        size=25,
        color=(255, 255, 0),
    )

    # highlights and effects for choice
    if controlador_jogo.is_choice_needed():
        choicefliter.draw()
        msg_selecione_alvo.set_position(
            RES_WIDTH / 2 - msg_selecione_alvo.width / 2, RES_HEIGHT * 0.75
        )
        msg_selecione_alvo.draw()
        # DRAW TARGETS OVER YELLOW FILTER
        for each in controlador_jogo.get_target_choices():
            each.get_hurtbox().draw()

    janela.update()
