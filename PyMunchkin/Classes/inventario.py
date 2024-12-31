class Inventario:
    def __init__(self):
        self.itens_equipados = {
            "headgear": [],
            "armor": [],
            "1hand": [],
            "2hands": [],
            "footgear": [],
            None: [],
        }
        self.itens_carregados = []
        self.itens_proibidos = []

    def equiparItem(self, item):

        if item.tipo in self.itens_equipados:
            print("discard " + self.itens_equipados[item.tipo].descricao)

        self.itens_equipados[item.tipo] = item
