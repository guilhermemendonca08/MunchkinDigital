# ========================================= MAJOR FIXES NEEDED (TODO LIST):
# +++CLICKS TRAVEL THROUGH STATES
# ++CHARITY STATE NOT IMPLEMENTED YET
# -STATES NEED MANUAL RESET
# +LOOT THE ROOM STAGE IS ROUGH
# ++++ LOOT THE ROOM SOMETIMES DOESN'T GIVE REWARDS. (NOT SURE WHY)
# --HIGHLIGHT PLAYABLE CARDS?
# -jogador tem add_card e "devolve_a_mao"
# ++++MAKE THE GAME OBNOXIOUSLY LOUD

# ==== Done list ====
# +SOUNDS ARE NOT PROPERLY RESET (Now they are)
# ++APPLY VICTORY/LOSS CONSEQUENCES. (Done)
# ++RESHUFFLE WHEN YOU TRY TO DRAW FROM EMPTY PILE (Harder than it seemed, but done)

import json
import io
from Imports.constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
    TREASURE_JSON_DATA,
    DUNGEON_JSON_DATA,
)
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.sound import Sound
from Imports.jogador import Jogador
from Imports.controlador_jogo import ControladorJogo
from Imports.Utils.card_factory import CardFactory
from path import resource_path

# ================================================================================================

# Inicialização da janela e objetos básicos.
janela = Window(RES_WIDTH, RES_HEIGHT)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

# Debug Hotkeys
hotkey_1 = False  # passa turno pra outro jogador
hotkey_2 = False  # +1 level
hotkey_3 = False  # carrega carta especifica no topo do deck.
hotkey_4 = False

# Input default
# mouse_click = False

# Assets Básicos
# GameImages estáticos.
print("heeeey")
print(resource_path("Assets/TableAssets/MarbleBlack.jpg"))
fundo = GameImage(resource_path("Assets/TableAssets/MarbleBlack.jpg"))
choicefliter = GameImage(resource_path("Assets/TableAssets/choice.png"))
borda = GameImage(resource_path("Assets/TableAssets/Border_Gray50.png"))
borda.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
displaynivel = Sprite(resource_path("Assets/Niveis/leveldisplay.png"), 10)
msg_selecione_alvo = GameImage(resource_path("Assets/TableAssets/select_target2.png"))

# SFX
hover = Sound(resource_path("Assets/SFX/sfx_card_hover.ogg"))
reject = Sound(resource_path("Assets/SFX/sfx_card_reject.ogg"))
select = Sound(resource_path("Assets/SFX/sfx_card_select.ogg"))
deal = Sound(resource_path("Assets/SFX/sfx_card_deal.ogg"))

# Elementos de controle do jogo.
controlador_jogo = ControladorJogo(janela)

# Carregamento de cartas
card_factory = CardFactory()
# Carrega cartas Tesouro
treasure_json_file = io.StringIO(TREASURE_JSON_DATA)  # Simula abertura do json
treasure_card_data = json.load(treasure_json_file)  # De json -> dict
treasure_cards = card_factory.carrega_cartas(treasure_card_data)  # dict -> lista
controlador_jogo.carrega_cartas(treasure_cards, controlador_jogo.get_deck_tesouro())

# Carrega cartas Dungeon
dungeon_json_file = io.StringIO(DUNGEON_JSON_DATA)
dungeon_card_data = json.load(dungeon_json_file)
dungeon_cards = card_factory.carrega_cartas(dungeon_card_data)
controlador_jogo.carrega_cartas(dungeon_cards, controlador_jogo.get_deck_dungeon())

# Carrega sons
controlador_jogo.set_sfx(hover, reject, select, deal)

# Inicia Jogadores
jogador1 = Jogador("Apollo", resource_path("Assets/Portraits/Archer.png"))
jogador2 = Jogador("Freya", resource_path("Assets/Portraits/HumanF4.png"))
jogador3 = Jogador("Antares", resource_path("Assets/Portraits/HumanM4.png"))
jogador4 = Jogador("Raphael", resource_path("Assets/Portraits/FiendM1.png"))

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
        controlador_jogo.proximo_turno()
    if not teclado.key_pressed("1"):
        hotkey_1 = False

    # Muda o nivel do personagem
    if teclado.key_pressed("2") and not hotkey_2:
        hotkey_2 = True
        # TODO: utilizar valor sentinela para evitar warning de variável None.
        controlador_jogo.get_jogador_atual().adiciona_ao_nivel_personagem(1)

    if not teclado.key_pressed("2"):
        hotkey_2 = False

    # Carrega carta especifica no topo do deck.
    if teclado.key_pressed("3") and not hotkey_3:
        hotkey_3 = True
        nome_carta = "Crabs"
        controlador_jogo.load_card_by_name_in_deck(nome_carta)
        print("loaded card:", nome_carta)

    if not teclado.key_pressed("3"):
        hotkey_3 = False

    # DEBUG 4
    if teclado.key_pressed("4") and not hotkey_4:
        hotkey_4 = True
        controlador_jogo.jogador_compra_carta(
            controlador_jogo.get_jogador_atual(), controlador_jogo.deck_tesouro
        )
        # Compra uma carta tipo tesouro.

    if not teclado.key_pressed("4"):
        hotkey_4 = False

    # Draws
    # Background, everything else should be placed AFTER this.
    fundo.draw()
    borda.draw()

    # Draw Players' Avatars
    avatar_offset_x = 0
    for each in controlador_jogo.jogadores:
        if each == controlador_jogo.get_jogador_atual():
            each.avatar.set_position(0, RES_HEIGHT - each.get_avatar_y())
            each.draw()
        else:
            each.avatar.set_position(0 + avatar_offset_x, 0)
            avatar_offset_x += RES_WIDTH / 3
            each.scaled_draw(100, 100)

    # Draw Players' Hands
    avatar_offset_x = 0
    for each in controlador_jogo.jogadores:
        if each == controlador_jogo.get_jogador_atual():
            each.draw_mao(RES_WIDTH / 2, RES_HEIGHT - CARD_HEIGHT)
        else:
            each.scaled_draw_mao(0 + avatar_offset_x, 100, 80, 124)
            avatar_offset_x += RES_WIDTH / 3

    # Draw Player's level
    avatar_offset_x = 0
    for each in controlador_jogo.jogadores:
        if each == controlador_jogo.get_jogador_atual():
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

    if controlador_jogo.get_jogador_atual() is None:
        player_stats_dict = {"No player present": "No player present"}
    else:
        # TODO: utilizar valor sentinela para evitar warning de variável None.
        player_stats_dict = controlador_jogo.get_jogador_atual().get_stats()

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
    controlador_jogo.executar_fase()

    # Debugging Text
    # Jogador da vez e Fase do turno
    jogadoratual = controlador_jogo.get_jogador_atual()
    if jogadoratual:
        player_turn_debug_text = jogadoratual.get_nome()
        player_turn_debug_text += "'s turn"
    else:
        player_turn_debug_text = "Nenhum jogador presente"
    phase_debug_text = controlador_jogo.get_estado_do_jogo()
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

    # =========================Start of Equipment Debugging Messages===========================
    # Equipamentos do jogador atual
    pos = 0
    text_equipamento_debug = "headgear"
    aux = controlador_jogo.get_jogador_atual().get_itens_em_slot("headgear")
    if aux:
        text_equipamento_debug += (
            ": " + aux[0].get_nome() + " +" + str(aux[0].get_poder())
        )
    janela.draw_text(
        text_equipamento_debug,
        1430,
        820,
        size=25,
        color=(255, 255, 0),
    )
    # ==============
    text_equipamento_debug = "armor"
    aux = None
    aux = controlador_jogo.get_jogador_atual().get_itens_em_slot("armor")
    pos += 30
    if aux:
        text_equipamento_debug += (
            ": " + aux[0].get_nome() + " +" + str(aux[0].get_poder())
        )
    janela.draw_text(
        text_equipamento_debug,
        1430,
        820 + pos,
        size=25,
        color=(255, 255, 0),
    )

    # ==============
    text_equipamento_debug = "footgear"
    aux = None
    aux = controlador_jogo.get_jogador_atual().get_itens_em_slot("footgear")
    pos += 30
    if aux:
        text_equipamento_debug += (
            ": " + aux[0].get_nome() + " +" + str(aux[0].get_poder())
        )
    janela.draw_text(
        text_equipamento_debug,
        1430,
        820 + pos,
        size=25,
        color=(255, 255, 0),
    )

    # ==============
    aux = None
    aux = controlador_jogo.get_jogador_atual().get_itens_em_slot("1hand")
    pos += 30
    text_equipamento_debug = "1 handed"
    janela.draw_text(
        text_equipamento_debug,
        1430,
        820 + pos,
        size=25,
        color=(255, 255, 0),
    )
    if aux:
        text_equipamento_debug = "1 handed:"
        janela.draw_text(
            text_equipamento_debug,
            1430,
            820 + pos,
            size=25,
            color=(255, 255, 0),
        )
        pos -= 30
        for each in aux:
            pos += 30
            text_equipamento_debug = each.get_nome() + " +" + str(each.get_poder())
            janela.draw_text(
                text_equipamento_debug,
                1550,
                820 + pos,
                size=25,
                color=(255, 255, 0),
            )

    # ==============
    text_equipamento_debug = "2 handed"
    aux = None
    aux = controlador_jogo.get_jogador_atual().get_itens_em_slot("2hands")
    pos += 30
    if aux:
        text_equipamento_debug += (
            ": " + aux[0].get_nome() + " +" + str(aux[0].get_poder())
        )
    janela.draw_text(
        text_equipamento_debug,
        1430,
        820 + pos,
        size=25,
        color=(255, 255, 0),
    )

    # ==============
    text_equipamento_debug = "None"
    aux = None
    aux = controlador_jogo.get_jogador_atual().get_itens_em_slot(None)
    pos += 30
    text_equipamento_debug = "No slot"
    janela.draw_text(
        text_equipamento_debug,
        1430,
        820 + pos,
        size=25,
        color=(255, 255, 0),
    )
    if aux:
        text_equipamento_debug = "No slot:"
        janela.draw_text(
            text_equipamento_debug,
            1430,
            820 + pos,
            size=25,
            color=(255, 255, 0),
        )
        pos -= 30
        for each in aux:
            pos += 30
            text_equipamento_debug = each.get_nome() + " +" + str(each.get_poder())
            janela.draw_text(
                text_equipamento_debug,
                1550,
                820 + pos,
                size=25,
                color=(255, 255, 0),
            )
    # ===========================End of Equipment Debugging Messages===========================

    # ===========================Debug Combate
    debug_combat_strenght = "Monstro: "
    if controlador_jogo.get_estado_do_jogo() == "Combate":
        debug_combat_strenght += str(
            controlador_jogo.gerenciador_combate.get_forca_monstros()
        )
        janela.draw_text(
            debug_combat_strenght,
            RES_WIDTH / 2,
            750,
            size=50,
            color=(255, 0, 0),
        )

    if controlador_jogo.get_estado_do_jogo() == "Combate":
        debug_combat_strength = controlador_jogo.gerenciador_combate.jogador[
            0
        ].get_nome()
        debug_combat_strength += ": "
        debug_combat_strength += str(
            controlador_jogo.gerenciador_combate.get_forca_jogadores()
        )
        janela.draw_text(
            debug_combat_strength,
            600,
            750,
            size=50,
            color=(255, 0, 0),
        )
    # ===========================Debug Pilhas de Cartas
    # Número de cartas nas pilhas.
    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_dungeon.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        RES_WIDTH * 25 / 32,
        RES_HEIGHT * 0.35,
        size=25,
        color=(255, 255, 0),
    )

    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_dungeon_discard.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        1700,
        RES_HEIGHT * 0.62,
        size=25,
        color=(255, 255, 0),
    )

    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_tesouro.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        10,
        RES_HEIGHT * 0.35,
        size=25,
        color=(255, 255, 0),
    )

    text_numero_de_cartas = "Cartas na pilha: "
    text_numero_de_cartas += str(controlador_jogo.deck_tesouro_discard.get_size())
    janela.draw_text(
        text_numero_de_cartas,
        240,
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

    # print(controlador_jogo.jogador_atual.request_gear("headgear"))
    janela.update()
