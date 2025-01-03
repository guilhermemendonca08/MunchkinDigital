from Imports.constants import (
    RES_WIDTH,
    RES_HEIGHT,
    CARD_WIDTH,
    CARD_HEIGHT,
)
from Imports.Estados.estado import Estado
from PPlay.gameimage import GameImage
from path import resource_path
from PPlay.sprite import Sprite
from PPlay.sound import Sound
from random import choice

# from PPlay.sound import Sound


class Caridade(Estado):
    def __init__(self):
        self.nome = "Caridade"
        self.cartas_aceitas = [
            "maldicao",
            "classe",
            "raca",
            "equipamento",
            "utilitario",
        ]
        self.mouse_state = False
        self.bg = GameImage(
            resource_path(resource_path("Assets/TableAssets/carta_caridade_alt.png"))
        )
        self.bg.set_position(
            RES_WIDTH / 2 - self.bg.width / 2, RES_HEIGHT / 2 - self.bg.height / 2
        )
        self.botao_ir_para_caridade = Sprite(
            resource_path("Assets/TableAssets/sprite_doar_excedentes.png"), 2
        )
        self.botao_ir_para_caridade.set_position(
            RES_WIDTH - 1.5 * self.botao_ir_para_caridade.width,
            RES_HEIGHT - 1.5 * self.botao_ir_para_caridade.height,
        )
        self.sfx_cartas_doadas = [
            Sound(resource_path("Assets/SFX/Charity/candy_from_a_baby.ogg")),
            Sound(resource_path("Assets/SFX/Charity/dont_mind_if_i_do.ogg")),
            Sound(resource_path("Assets/SFX/Charity/gimme_gimme.ogg")),
            Sound(resource_path("Assets/SFX/Charity/i_was_meant_to_have_this.ogg")),
            Sound(resource_path("Assets/SFX/Charity/one_for_me.ogg")),
            Sound(resource_path("Assets/SFX/Charity/transaction_complete.ogg")),
            Sound(resource_path("Assets/SFX/Charity/we_got_the_goods.ogg")),
        ]
        self.sfx_cartas_cobranca = [
            Sound(resource_path("Assets/SFX/Charity/gotta_get_my_cut.ogg")),
            Sound(resource_path("Assets/SFX/Charity/i_come_to_collect.ogg")),
            Sound(resource_path("Assets/SFX/Charity/mine_selfish.ogg")),
            Sound(resource_path("Assets/SFX/Charity/oh_shiny.ogg")),
            Sound(resource_path("Assets/SFX/Charity/split_the_loot.ogg")),
            Sound(resource_path("Assets/SFX/Charity/well_split_this.ogg")),
            Sound(resource_path("Assets/SFX/Charity/well_take_that.ogg")),
        ]
        self.intro_sfx = False

    def reset(self):
        self.__init__()

    def executa_fase(self, controlador):
        if not self.intro_sfx:
            self.intro_sfx = True
            choice(self.sfx_cartas_cobranca).play()
        self.bg.draw()
        self.botao_ir_para_caridade.draw()
        if controlador.mouse_over_object(self.botao_ir_para_caridade):
            self.botao_ir_para_caridade.set_curr_frame(1)
        else:
            self.botao_ir_para_caridade.set_curr_frame(0)

        if (
            not controlador.mouse_input.is_button_pressed(1)
            and self.mouse_state
            and controlador.mouse_over_object(self.botao_ir_para_caridade)
            and controlador.is_their_turn()
        ):

            self.mouse_state = False
            choice(self.sfx_cartas_doadas).play()
            # Doa cartas excedentes
            jogador = controlador.get_jogador_ativo()
            if jogador.get_size_mao() > 5:
                jogadores_restantes = controlador.get_lista_jogadores()
                menor_nivel = 10
                for each in jogadores_restantes:
                    if each.get_nivel_personagem() < menor_nivel:
                        menor_nivel = each.get_nivel_personagem()

                candidatos = []
                for each in jogadores_restantes:
                    if (
                        each.get_nivel_personagem() == menor_nivel
                        and each.get_nome() != jogador.get_nome()
                    ):
                        candidatos.append(each)

                mao = jogador.get_mao()
                for _ in range(jogador.get_size_mao() - 5):
                    carta = choice(mao)
                    jogador.remove_card(carta)
                    choice(candidatos).add_card(carta)

            # Segue com próximo jogador
            controlador.set_jogador_ativo(
                controlador.proximo_depois_de(controlador.get_jogador_ativo())
            )
            controlador.set_jogador_atual(controlador.get_jogador_ativo())
            controlador.proximo_estado("ChutarPorta")

        # Atualiza estado anterior do mouse
        if controlador.mouse_input.is_button_pressed(1):
            self.mouse_state = True
        else:
            self.mouse_state = False

    def get_estado_do_jogo(self):
        return self.nome

    def aceita_carta(self, carta):
        if carta.get_tipo() in self.cartas_aceitas:
            return True
        else:
            return False
