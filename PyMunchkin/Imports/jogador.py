from Imports.observer import Observer
from Imports.constants import CARD_WIDTH
from PPlay.gameimage import GameImage
from Imports.personagem import Personagem
from Imports.inventario import Inventario
from path import resource_path
from Imports.targetable import Targetable
from random import choice


class Jogador(Observer, Targetable):
    def __init__(self, nome, avatar_image):
        self.avatar = GameImage(resource_path(avatar_image))
        self.nome = nome
        self.personagem = Personagem()
        self.mao = []
        self.inventario = Inventario()
        self._discard_callback = None

    # Equip stuff
    def morrer(self):
        gear_list = self.request_gear(["any"])
        for each in gear_list:
            self.desequipar_item(each)
        # self.personagem.morrer()

    def request_gear(self, param):
        itens = []
        print(f"param: {param}")
        for p in param:
            print(f"p: {p}")
            if p in {"big", "small"}:
                itens += self.inventario.get_itens_por_tamanho(p)
            else:
                itens += self.inventario.get_itens_em_slot(p)
        # print(f"Pedi itens de {param} e recebi {itens}")
        # print(f"Em contraste: {self.inventario.get_itens_em_slot("headgear")}")
        return itens

    def get_itens_em_slot(self, slot):
        return self.inventario.get_itens_em_slot(slot)

    def equipar_classe(self, classe):
        if self.personagem.get_classe() is not None:
            self.discard(self.personagem.get_classe())
        self.personagem.equipar_classe(classe)

    def equipar_raca(self, raca):
        if self.personagem.get_raca() is not None:
            self.discard(self.personagem.get_raca())
        self.personagem.equipar_raca(raca)

    def equipar_item(self, item):
        slot_item_novo = item.get_slot()
        if self.inventario.tem_espaco_para_equipar(item):
            self.inventario.equipar_item(item)
        else:
            item_a_remover = [item]
            if slot_item_novo in {"headgear", "armor", "footgear"}:
                if [item.get_poder()] >= self.inventario.get_poder_no_slot(
                    slot_item_novo
                ):
                    item_a_remover = self.inventario.get_itens_em_slot(slot_item_novo)
            elif slot_item_novo == "1hand":
                #  Equipar 1 arma de 1 mão vs duas armas de uma mão
                if len(self.inventario.get_itens_em_slot("1hand")) == 2:
                    for each in self.inventario.get_itens_em_slot("1hand"):
                        if item_a_remover[0].get_poder() >= each.get_poder():
                            item_a_remover[0] = each
                # Equipar 1 arma de uma mão vs uma arma de duas mãos
                elif len(self.inventario.get_itens_em_slot("2hands")) == 1:
                    for each in self.inventario.get_itens_em_slot("2hands"):
                        if item_a_remover[0].get_poder() >= each.get_poder() // 2:
                            item_a_remover[0] = each
                else:
                    raise ValueError("Why are we still here… Just to suffer? ")
            elif slot_item_novo == "2hands":
                # Equipar uma arma de 2 mãos vs pelo menos uma arma de 1 mão
                if len(self.inventario.get_itens_em_slot("1hand")) >= 1:
                    soma_poder = 0
                    for each in self.inventario.get_itens_em_slot("1hand"):
                        soma_poder += each.get_poder()
                    if item_a_remover[0].get_poder() >= soma_poder:
                        item_a_remover = self.inventario.get_itens_em_slot("1hand")
                # Equipar uma arma de 2 mãos vs uma arma de 2 mãos
                elif len(self.inventario.get_itens_em_slot("2hands")) == 1:
                    for each in self.inventario.get_itens_em_slot("2hands"):
                        if item_a_remover[0].get_poder() >= each.get_poder():
                            item_a_remover[0] = each
                else:
                    raise ValueError("Why are we still here… Just to suffer? again?")
            if item_a_remover[0] != item:
                for each in item_a_remover:
                    print(f"Tentando desequipar {each.get_nome()}")
                    if self.inventario.desequipar_item(each):
                        print(f"Desquipou {each.get_nome()}")
                        self.discard(each)
                self.inventario.equipar_item(item)
            else:
                self.add_card(item)
                print("devolver a mao para a carta nao ser jogada")

    # Set Discard Callback.
    def set_discard_callback(self, callback):
        self._discard_callback = callback

    def discard(self, card):
        """NÃO RETIRA CARTA DA MÃO, APENAS DESCARTA. (DEVOLVE A PILHA)
        TROCAR NOME??
        """
        # TODO: utilizar valor sentinela para evitar warning de variável None.
        self._discard_callback(card)

    def discard_raca(self):
        if self.personagem.get_raca() is not None:
            self.discard(self.personagem.get_raca())
            self.personagem.equipar_raca(None)

    def discard_classe(self):
        if self.personagem.get_classe() is not None:
            self.discard(self.personagem.get_classe())
            self.personagem.equipar_classe(None)

    # Apenas descarta cartas da mão pois "carregar" foi apenas
    # parcialmente implementada.
    def descarta_cartas(self, quantidade):
        if quantidade > self.get_size_mao():
            quantidade = self.get_size_mao()
        for _ in range(quantidade):
            carta = choice(self.mao)
            self.discard(carta)
            self.mao.remove(carta)

    # Avatar stuff
    def get_hurtbox(self):
        return self.avatar

    def adiciona_ao_nivel_personagem(self, quantidade):
        self.personagem.adiciona_ao_nivel(quantidade)

    def set_avatar_position(self, x, y):
        self.avatar.set_position(x, y)

    def get_avatar_x(self):
        return self.avatar.width

    def get_avatar_y(self):
        return self.avatar.height

    def get_nome(self):
        return self.nome

    # Stats
    def get_nivel_personagem(self):
        return self.personagem.get_nivel()

    def get_stats(self):
        stats = {}
        stats["Nome"] = self.nome
        stats["Nivel"] = self.get_nivel_personagem()
        stats["Raca"] = (
            self.personagem.get_raca().get_nome_raca()
            if (self.personagem.get_raca() is not None)
            else "Humano"
        )
        stats["Classe"] = (
            self.personagem.get_classe().get_nome_classe()
            if (self.personagem.get_classe() is not None)
            else "Nenhuma"
        )
        stats["Forca de Combate"] = self.calcular_forca_combate()
        return stats

    def get_character_level(self):
        return self.personagem.get_nivel()

    def level_up(self):
        self.personagem.adiciona_ao_nivel(1)

    # Combate

    def aplicar_buff(self, valor):
        self.personagem.aplicar_buff(valor)

    def reseta_buffs(self):
        self.personagem.reseta_buffs()

    def calcular_forca_combate(self):
        somatorio = 0
        somatorio += self.personagem.calcular_forca_combate()
        somatorio += self.inventario.get_bonus_combate()
        return somatorio

    def fugir(self, monstro):
        pass

    # Iventory Management
    def desequipar_item(self, item):
        if self.inventario.desequipar_item(item):
            self.discard(item)

    # def desequipar_item(self, item):
    #     self.discard(item)
    #     # self.inventario.remove(item)
    #     self.inventario.desequipar_item(item)

    # Card Managment
    def jogar_carta(self, carta, alvo):
        self.remove_card(carta)  # Remove a carta da mão do jogador
        carta.jogar_carta(alvo)
        self.add_card(carta)
        if carta.get_tipo() in {"combate", "maldicao", "utilitario"}:
            self.discard(carta)

    def has_card(self, card):
        return card in self.mao

    def add_card(self, card):
        self.mao.append(card)

    def remove_card(self, card):
        self.mao.remove(card)

    def receber_carta(self, carta):
        self.mao.append(carta)

    def get_size_mao(self):
        return len(self.mao)

    # PPLAY STUFF
    # Draws
    def draw(self):
        self.avatar.draw()

    def scaled_draw(self, new_width, new_height):
        self.avatar.scaled_draw(new_width, new_height)

    def draw_mao(self, offset_x, offset_y):
        peek_window = 100
        hand_pixel_size = peek_window * (self.get_size_mao() - 1) + CARD_WIDTH
        for i, card in enumerate(self.mao):
            card.set_position(
                offset_x + (-hand_pixel_size / 2 + i * peek_window), offset_y + 0
            )
            card.draw()

    def scaled_draw_mao(self, offset_x, offset_y, new_width, new_height):
        peek_window = 60
        for i, card in enumerate(self.mao):
            card.set_position(offset_x + (i * peek_window), offset_y + 0)
            card.scaled_draw(new_width, new_height)

    # SUBJECT/ OBSERVER PATTERN
    def update(self, estado_do_jogo, jogador_atual, carta_em_jogo):
        pass
