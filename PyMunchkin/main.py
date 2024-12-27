from PPlay.gameimage import GameImage
from PPlay.window import Window
from Classes.jogador import Jogador
from Classes.carta_item import Item
from Classes.controladorjogo import ControladorJogo

# Inicialização da janela e objetos básicos.
res_width = 1920
res_height = 1080
janela = Window(res_width, res_height)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

# GameImages de estéticos.
fundo = GameImage("Assets/TableAssets/MarbleBlack.jpg")
borda = GameImage("Assets/TableAssets/Border_Gray50.png")
borda.set_position(res_width / 4, res_height / 4)
closeddoor = GameImage("Assets/TableAssets/ClosedDoor50.png")
closeddoor.set_position(res_width / 4, res_height / 4)

# Elementos de controle do jogo.
controladorJogo = ControladorJogo()

# Carregamento de informações
controladorJogo.carregaCartas()


# player1 = GameImage("Assets/Portraits/Archer.png")
# player1.set_position(0, res_height - player1.height)
# player1 = Jogador("Guilherme", None, None, "Assets/Portraits/Archer.png")
# player1.set_position(0, res_height - player1.gimage.height)

# Variaveis de apoio.
time_acc = 0

while True:
    dt = janela.delta_time()
    time_acc += dt

    # Draws
    fundo.draw()
    closeddoor.draw()
    borda.draw()
    controladorJogo.deckTesouro[0].imagem.draw()

    # Debugging Text
    player_turn_debug_text = controladorJogo.get_jogadorAtual()
    phase_debug_text = controladorJogo.get_estadoDoJogo()
    janela.draw_text(
        player_turn_debug_text,
        res_width - 14 * len(player_turn_debug_text),
        res_height - 60,
        size=25,
        color=(255, 255, 0),
    )
    janela.draw_text(
        phase_debug_text,
        res_width - 12 * len(phase_debug_text),
        res_height - 30,
        size=25,
        color=(255, 255, 0),
    )

    janela.update()
