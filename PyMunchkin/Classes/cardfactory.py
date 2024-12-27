class CardFactory:
    def create_card(id, cardtype, effect):
        if cardtype == "Item":
            return Item(id, effect)
        elif cardtype == "Monstro":
            return Monster(id, effect)
        elif cardtype == "Maldicao":
            return Spell(id, effect)
        elif cardtype == "Amplificador":
            return Spell(id, effect)
        elif cardtype == "Raca":
            return Spell(id, effect)
        else:
            return None
