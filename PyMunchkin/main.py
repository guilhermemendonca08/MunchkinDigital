from constants import RES_WIDTH, RES_HEIGHT, CARD_HEIGHT
from PPlay.gameimage import GameImage
from PPlay.window import Window
from Classes.jogador import Jogador
from Classes.controladorjogo import ControladorJogo

# from constants import CARD_WIDTH, CARD_HEIGHT
# from Classes.carta_item import Item

# Inicialização da janela e objetos básicos.
janela = Window(RES_WIDTH, RES_HEIGHT)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

# GameImages de estéticos.
fundo = GameImage("Assets/TableAssets/MarbleBlack.jpg")
borda = GameImage("Assets/TableAssets/Border_Gray50.png")
borda.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)
closeddoor = GameImage("Assets/TableAssets/ClosedDoor50.png")
closeddoor.set_position(RES_WIDTH / 4, RES_HEIGHT / 4)

# Elementos de controle do jogo.
controladorJogo = ControladorJogo()
# Carregamento de informações
controladorJogo.carregaCartas()

# Inicia Jogador
jogador1 = Jogador("Guilherme", "Assets/Portraits/Archer.png")
jogador1.set_position(0, RES_HEIGHT - jogador1.get_avatar_y())

# Variaveis de apoio.
time_acc = 0

controladorJogo.add_jogador(jogador1)
controladorJogo.executarFase()
while True:
    dt = janela.delta_time()
    time_acc += dt

    # Draws
    fundo.draw()
    closeddoor.draw()
    borda.draw()
    # Draw Players
    jogador1.draw()

    # Draw Cards
    jogador1.draw_mao(RES_WIDTH / 2, RES_HEIGHT - CARD_HEIGHT)

    # Debugging Text
    player_turn_debug_text = controladorJogo.get_jogadorAtual()
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
