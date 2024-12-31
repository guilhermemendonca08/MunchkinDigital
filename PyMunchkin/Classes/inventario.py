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

    # Getters
    def get_itens_em_slot(self, slot):
        return self.itens_equipados[slot]

    def get_poder_no_slot(self, slot):
        poderes_em_slot = []
        for item in self.itens_equipados[slot]:
            poderes_em_slot.append(item.get_poder())
        return poderes_em_slot

    # Equipa/desequipa itens
    def tem_espaco_para_equipar(self, item):
        item_slot = item.get_slot()
        if item_slot is None:
            return True
        if item_slot in {"1hand", "2hands"}:
            occupied_hands = len(self.itens_equipados["1hand"]) + 2 * len(
                self.itens_equipados["2hands"]
            )
            if occupied_hands >= 2:
                return False
            if occupied_hands == 0:
                return True
            if item_slot == "1hand":
                return True
            if item_slot == "2hands":
                return False
        if item_slot in {"headgear", "armor", "footgear"}:
            return len(self.itens_equipados[item_slot]) == 0
        raise ValueError(f"Item com slot inválido: {item_slot}")

    def equipar_item(self, item):
        if item in self.itens_proibidos:
            return False
        if self.tem_espaco_para_equipar(item):
            self.itens_equipados[item.get_slot()].append(item)
            return True
        return False

    # Não descarta a carta (devolve a pilha, lembrar de implementar no jogador)
    def desequipar_item(self, item):
        if item in self.itens_equipados[item.get_slot()]:
            self.itens_equipados[item.get_slot()].remove(item)
            return True
        else:
            return False
            raise ValueError("Tentativa de remover item não equipado.")

    # adiciona/remove itens carregados
    def adicionar_item_carregado(self, item):
        self.itens_carregados.append(item)

    def remove_item_carregado(self, item):
        if item in self.itens_carregados:
            self.itens_carregados.remove(item)
        else:
            raise ValueError("Tentativa de remover item não carregado.")
