from Classes.carta_item import Item
from Classes.carta_monstro import Monstro
from Classes.carta_maldicao import Maldicao
from Classes.carta_raca import Raca
from Classes.carta_amplificador import Amplificador
from Classes.efeito import Buff
from Classes.efeito import AddToLevel
from Classes.efeito import DiscardGear
from Classes.efeito import DiscardCards
from Classes.efeito import DiscardRaca
from Classes.efeito import DiscardClasse
from Classes.efeito import Death
from Classes.efeito import Equip
from Classes.classe_clerigo import Clerigo
from Classes.classe_guerreiro import Guerreiro
from Classes.classe_ladrao import Ladrao
from Classes.classe_mago import Mago


class CardFactory:
    def __init__(self):
        self.cardtypes = {
            "item": Item,
            "monstro": Monstro,
            "maldicao": Maldicao,
            # "classe": Classe,
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
