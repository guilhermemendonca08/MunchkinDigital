from Imports.Estados.estado import Estado


class Inicializacao(Estado):
    def __init__(self):
        self.nome = "Inicializacao"

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        print("Executando fase", controlador.get_estado_do_jogo())
        jogador = controlador.jogadores.proximo()
        controlador.set_jogador_atual(jogador)
        controlador.set_jogador_ativo(jogador)

        for each in controlador.jogadores:
            for _ in range(4):
                each.add_card(controlador.comprar_carta(controlador.deck_tesouro))
            for _ in range(4):
                each.add_card(controlador.comprar_carta(controlador.deck_dungeon))
            print(f"Jogador {each.get_nome()} recebeu {each.get_size_mao()} cartas")
        controlador.proximo_estado("ChutarPorta")

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        return False
