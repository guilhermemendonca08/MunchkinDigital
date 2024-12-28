from constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_HEIGHT,
    DOOR_HURTBOX_OFFSET_X,
    DOOR_HURTBOX_OFFSET_Y,
)
from PPlay.gameimage import GameImage
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
hotkey_1 = False
hotkey_2 = False
hotkey_3 = False
hotkey_4 = False

# Input default
mouse_click = False

# GameImages estáticos.
fundo = GameImage("Assets/TableAssets/MarbleBlack.jpg")
borda = GameImage("Assets/TableAssets/Border_Gray50.png")
borda.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
closeddoor = GameImage("Assets/TableAssets/ClosedDoor50.png")
closeddoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
doorhurtbox = GameImage("Assets/TableAssets/DoorHurtBoxSemiTransparent.png")
doorhurtbox.set_position(
    RES_WIDTH / 4 + DOOR_HURTBOX_OFFSET_X, RES_HEIGHT / 4 + DOOR_HURTBOX_OFFSET_Y
)

# Elementos de controle do jogo.
controladorJogo = ControladorJogo()
uihandler = UIHandler(mouse, controladorJogo)

# Carregamento de informações
controladorJogo.carregaCartas()

# Inicia Jogador
jogador1 = Jogador("Apollo", "Assets/Portraits/Archer.png")
jogador1.set_position(0, RES_HEIGHT - jogador1.get_avatar_y())

jogador2 = Jogador("Freya", "Assets/Portraits/HumanF4 (small).png")
jogador2.set_position(0, 0)

# Variaveis de apoio.
time_acc = 0

controladorJogo.add_jogador(jogador1)
controladorJogo.add_jogador(jogador2)
while True:
    controladorJogo.executarFase()
    dt = janela.delta_time()
    time_acc += dt

    # Eventos
    target = uihandler.mouse_over_card()

    if mouse.is_button_pressed(1):
        mouse_click = True

    if (mouse_click) and (not mouse.is_button_pressed(1)):
        mouse_click = False
        if target:
            print(f"I play {target.get_nome()}!")
            jogador1.remove_card(target)

    if time_acc >= 0.2:
        time_acc = 0

    # Debugging Events
    if teclado.key_pressed("1") and not hotkey_1:
        hotkey_1 = True
        controladorJogo.proximoTurno()
        # Do something
    if not teclado.key_pressed("1"):
        hotkey_1 = False

    # Draws
    fundo.draw()
    closeddoor.draw()
    doorhurtbox.draw()
    borda.draw()

    # Draw Players
    jogador1.draw()
    jogador2.draw()

    # Draw Cards
    jogador1.draw_mao(RES_WIDTH / 2, RES_HEIGHT - CARD_HEIGHT)

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
