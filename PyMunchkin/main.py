from constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
    DOOR_HURTBOX_OFFSET_X,
    DOOR_HURTBOX_OFFSET_Y,
)
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.window import Window
from Classes.jogador import Jogador
from Classes.controladorjogo import ControladorJogo
from Classes.ui_handler import UIHandler

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
mouse_click = False

# GameImages estáticos.
fundo = GameImage("Assets/TableAssets/MarbleBlack.jpg")
borda = GameImage("Assets/TableAssets/Border_Gray50.png")
borda.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
displaynivel = Sprite("Assets/Niveis/leveldisplay.png", 10)

# Elementos de controle do jogo.
# controladorJogo = ControladorJogo(mouse)
controladorJogo = ControladorJogo(janela)
# uihandler = UIHandler(mouse)
# controladorJogo.set_uihandler(uihandler)

# Carregamento de informações
controladorJogo.carregaCartas()

# Inicia Jogador
jogador1 = Jogador("Apollo", "Assets/Portraits/Archer.png")
# jogador1.set_avatar_position(0, RES_HEIGHT - jogador1.get_avatar_y())

jogador2 = Jogador("Freya", "Assets/Portraits/HumanF4.png")
# jogador2.set_avatar_position(0, 0)

jogador3 = Jogador("Antares", "Assets/Portraits/HumanM4.png")
# jogador3.set_avatar_position(0, 0)

jogador4 = Jogador("Raphael", "Assets/Portraits/FiendM1.png")
# jogador4.set_avatar_position(0, 0)
# Variaveis de apoio.
time_acc = 0

controladorJogo.add_jogador(jogador1)
controladorJogo.add_jogador(jogador2)
controladorJogo.add_jogador(jogador3)
controladorJogo.add_jogador(jogador4)
while True:
    dt = janela.delta_time()
    time_acc += dt

    # Eventos
    target = controladorJogo.mouse_over_card()

    if mouse.is_button_pressed(1):
        mouse_click = True

    if (mouse_click) and (not mouse.is_button_pressed(1)):
        mouse_click = False
        if target:
            if jogador1.has_card(target):
                print(f"I play {target.get_nome()}!")
                jogador1.remove_card(target)
            else:
                print(f"{target.get_descricao()}")

    # Debugging Events
    # Muda de quem é a vez.
    if teclado.key_pressed("1") and not hotkey_1:
        hotkey_1 = True
        controladorJogo.proximoTurno()
    if not teclado.key_pressed("1"):
        hotkey_1 = False

    # Muda o nivel do personagem
    if teclado.key_pressed("2") and not hotkey_2:
        hotkey_2 = True
        controladorJogo.get_jogadorAtual().mudarNivelPersonagem(1)

    if not teclado.key_pressed("2"):
        hotkey_2 = False
    # Draws
    # Background, everything else should be placed AFTER this.
    fundo.draw()

    borda.draw()

    # Draw Players' Avatars
    avatar_offset_x = 0
    for each in controladorJogo.jogadores:
        if each == controladorJogo.get_jogadorAtual():
            each.avatar.set_position(0, RES_HEIGHT - each.get_avatar_y())
            each.draw()
        else:
            each.avatar.set_position(0 + avatar_offset_x, 0)
            avatar_offset_x += RES_WIDTH / 3
            each.scaled_draw(100, 100)

    # Draw Players' Hands
    avatar_offset_x = 0
    for each in controladorJogo.jogadores:
        if each == controladorJogo.get_jogadorAtual():
            each.draw_mao(RES_WIDTH / 2, RES_HEIGHT - CARD_HEIGHT)
        else:
            each.scaled_draw_mao(0 + avatar_offset_x, 100, 80, 124)
            avatar_offset_x += RES_WIDTH / 3

    # Draw Player's level
    avatar_offset_x = 0
    for each in controladorJogo.jogadores:
        if each == controladorJogo.get_jogadorAtual():
            displaynivel.set_position(each.get_avatar_x(), RES_HEIGHT - 100)
            displaynivel.set_curr_frame(each.getNivelPersonagem() - 1)
            displaynivel.draw()
        else:
            displaynivel.set_position(100 + avatar_offset_x, 0)
            displaynivel.set_curr_frame(each.getNivelPersonagem() - 1)
            displaynivel.draw()
            avatar_offset_x += RES_WIDTH / 3

    # Draw Card Stacks
    # Door Pile
    controladorJogo.deckDungeon.set_position(
        RES_WIDTH - 2.5 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controladorJogo.deckDungeon.draw()

    # Door Discard Pile
    controladorJogo.deckDungeonDiscard.set_position(
        RES_WIDTH - 1.25 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controladorJogo.deckDungeonDiscard.draw()

    # Treasure Pile
    controladorJogo.deckTesouro.set_position(
        0.25 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controladorJogo.deckTesouro.draw()

    # Treasure Discard Pile
    controladorJogo.deckTesouroDiscard.set_position(
        1.5 * CARD_WIDTH, RES_HEIGHT / 2 - CARD_HEIGHT / 2
    )
    controladorJogo.deckTesouroDiscard.draw()

    # Game Logic / Draws from phases
    controladorJogo.executarFase()

    # Debugging Text
    jogadoratual = controladorJogo.get_jogadorAtual()
    if jogadoratual:
        player_turn_debug_text = jogadoratual.get_nome()
        player_turn_debug_text += "'s turn"
    else:
        player_turn_debug_text = "Nenhum jogador presente"
    phase_debug_text = controladorJogo.get_estadoDoJogo()
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

    janela.update()
