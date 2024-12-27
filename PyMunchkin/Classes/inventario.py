class Inventario:
    def __init__(self):
        self.itensEquipados = {}
        self.itensCarregados = []
        self.itensProibidos = []

    def equiparItem(self, item):

        if item.tipo in self.itensEquipados:
            print("discard " + self.itensEquipados[item.tipo].descricao)

        self.itensEquipados[item.tipo] = item
