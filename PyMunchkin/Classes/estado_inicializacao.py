from Classes.estado import Estado


class Inicializacao(Estado):
    def __init__(self):
        self.nome = "Inicializacao"

    def executa_fase(self, controlador):
        print("Executando fase", controlador.get_estadoDoJogo())
        controlador.set_jogadorAtual(controlador.jogadores.proximo())

        for each in controlador.jogadores:
            for _ in range(4):
                each.receber_carta(controlador.comprarCarta(controlador.deck_tesouro))
            for _ in range(4):
                each.receber_carta(controlador.comprarCarta(controlador.deck_dungeon))
            print(f"Jogador {each.get_nome()} recebeu {each.get_size_mao()} cartas")
        controlador.proximoEstado("ChutarPorta")

    def get_estado_do_jogo(self):
        return self.nome


    def aceita_carta(self, carta):
        return False
