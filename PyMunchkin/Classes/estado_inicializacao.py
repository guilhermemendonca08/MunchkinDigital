from Classes.estado import Estado


class Inicializacao(Estado):
    def __init__(self):
        self.nome = "Inicializacao"

    def executaFase(self, controlador):
        print("Executando fase", controlador.get_estadoDoJogo())

        for each in controlador.jogadores:
            for _ in range(4):
                each.receber_carta(controlador.comprarCarta(controlador.deckDungeon))
                each.receber_carta(controlador.comprarCarta(controlador.deckTesouro))
            print(f"Jogador {each.get_nome()} recebeu {each.get_size_mao()} cartas")

    def comprarCarta(self, deck):
        # print("Executando fase", controlador.get_estadoDoJogo())
        pass

    def get_faseDoJogo(self):
        return self.nome
