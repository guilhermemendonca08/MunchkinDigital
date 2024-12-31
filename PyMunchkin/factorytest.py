from constants import TREASURE_JSON_DATA
from constants import DUNGEON_JSON_DATA
import json
import io
from Classes.card_factory import CardFactory
from PPlay.window import Window

# Inicialização da janela e objetos básicos.
janela = Window(1920, 1080)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

# pseudo_json_file = io.StringIO(TREASURE_JSON_DATA)
pseudo_json_file = io.StringIO(DUNGEON_JSON_DATA)
data = json.load(pseudo_json_file)
# print(data)

cf = CardFactory()
cards = cf.carrega_cartas(data)

for each in cards:
    each.debug()
    print("----------------------")
    # print(each.get_nome())
    # print(f"valor: {each.efeito.valor}")
    # print(each.efeito.debug())
print(len(cards))

