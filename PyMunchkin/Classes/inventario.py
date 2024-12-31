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

    def desequipar_item(self, item):
        if item in self.itens_equipados[item.get_slot()]:
            self.itens_equipados[item.get_slot()].remove(item)
        else:
            raise ValueError("Tentativa de remover item não equipado.")

    def equipar_item(self, item):
        if item in self.itens_proibidos:
            return False
        if item.get_slot() in self.itens_equipados:
            self.itens_equipados[item.get_tipo()].append(item)
            return True
        return False
