from Imports.Cartas.carta_item import Item
from Imports.Cartas.carta_monstro import Monstro
from Imports.Cartas.carta_maldicao import Maldicao
from Imports.Cartas.carta_raca import Raca
from Imports.Cartas.carta_amplificador import Amplificador
from Imports.efeito import Buff
from Imports.efeito import AddToLevel
from Imports.efeito import DiscardGear
from Imports.efeito import DiscardCards
from Imports.efeito import DiscardRaca
from Imports.efeito import DiscardClasse
from Imports.efeito import Death
from Imports.efeito import Equip
from Imports.Cartas.Classes.classe_clerigo import Clerigo
from Imports.Cartas.Classes.classe_guerreiro import Guerreiro
from Imports.Cartas.Classes.classe_ladrao import Ladrao
from Imports.Cartas.Classes.classe_mago import Mago


class CardFactory:
    def __init__(self):
        self.cardtypes = {
            "item": Item,
            "monstro": Monstro,
            "maldicao": Maldicao,
            "raca": Raca,
            "amplificador": Amplificador,
            "clerigo": Clerigo,
            "guerreiro": Guerreiro,
            "ladrao": Ladrao,
            "mago": Mago,
        }
        self.efeitos = {
            "buff": Buff,
            "addtolevel": AddToLevel,
            "discardcards": DiscardCards,
            "discardgear": DiscardGear,
            "discardrace": DiscardRaca,
            "discardclass": DiscardClasse,
            "death": Death,
            "equipar": Equip,
        }

    def carrega_efeito(self, id_efeito, **kwargs):
        """
        Função que carrega o efeito da carta
        :param id_efeito: ID do efeito
        :param kwargs: Argumentos do efeito
        :return: Efeito
        """
        effectclass = self.efeitos.get(id_efeito)
        if not effectclass:
            raise ValueError(f"Efeito inválido: {id_efeito}")
        if not kwargs:
            return effectclass()
        return effectclass(**kwargs)

    def carrega_carta(self, card_data):
        """
        Função que carrega uma carta do jogo
        :param card_data: Dicionário contendo as informações da carta
        :return: Carta
        """
        cardtype = card_data["type"]
        cardclass = self.cardtypes.get(cardtype)
        if not cardclass:
            raise ValueError(f"Tipo de carta inválido: {cardtype}")
        return cardclass(**card_data["attributes"])

    def carrega_cartas(self, cards_dict):
        """
        Função que carrega as cartas do jogo
        :param card_data: Dicionário contendo as informações das cartas
        :return: Lista de cartas
        """
        cards = []
        for card_data in cards_dict:
            # if "efeito" in card_data["attributes"]:
            if card_data["attributes"].get("efeito"):
                if card_data["attributes"].get("parameters", {}):
                    card_data["attributes"]["efeito"] = self.carrega_efeito(
                        card_data["attributes"]["efeito"],
                        **card_data["attributes"].get("parameters", {}),
                    )
                else:
                    card_data["attributes"]["efeito"] = self.carrega_efeito(
                        card_data["attributes"]["efeito"]
                    )
            card_data["attributes"].pop("parameters", None)
            card = self.carrega_carta(card_data)
            cards.append(card)
        return cards

    # def carrega_cartas(self, card_data):
    #     """
    #     Função que carrega as cartas do jogo
    #     :param card_data: Dicionário contendo as informações das cartas
    #     :return: Lista de cartas
    #     """
    #     cards = []
    #     for data in card_data:
    #         cardtype = data["tipo"]  # Pega o tipo da carta (ex: item)
    #         cardclass = self.cardtypes.get(
    #             cardtype
    #         )  # Pega a classe da carta (ex: Item)
    #         if not cardclass:
    #             raise ValueError(f"Tipo de carta inválido: {cardtype}")
    #         cards.append(
    #             cardclass(**data["atributos"])
    #         )  # Cria a carta com os atributos passados
    #     return cards
