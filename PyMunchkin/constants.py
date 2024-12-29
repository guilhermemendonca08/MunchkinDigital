CARD_WIDTH = 160
CARD_HEIGHT = 248
RES_WIDTH = 1920
RES_HEIGHT = 1080
DOOR_HURTBOX_OFFSET_X = 346
DOOR_HURTBOX_OFFSET_Y = 74

TREASURE_JSON_DATA = """
[
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/101 (small).png",
            "nome": "Magic Missile",
            "descricao": "Use during combat. +5 to either side. Usable only once",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 300,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 5}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/103 (small).png",
            "nome": "Potion of Halitosis",
            "descricao": "Bad Breath",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 100,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 2}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/104 (small).png",
            "nome": "Swiss Army Polearm",
            "descricao": "Usable by Human Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 4,
            "tamanho": "big",
            "valor": 600,
            "restricao": "human",
            "usoUnico": false,
            "slot": "2hands",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/105 (small).png",
            "nome": "Buckler of Swashing",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 2,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/108 (small).png",
            "nome": "Slimy Armor",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 200,
            "restricao": null,
            "usoUnico": false,
            "slot": "armor",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/109 (small).png",
            "nome": "Bad-Ass Bandana",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": "headgear",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/111 (small).png",
            "nome": "Dagger of Treachery",
            "descricao": "Usable by Thief Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 400,
            "restricao": "thief",
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/113 (small).png",
            "nome": "Chainsaw of Bloody Dismemberment",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "big",
            "valor": 600,
            "restricao": null,
            "usoUnico": false,
            "slot": "2hands",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/115 (small).png",
            "nome": "Boots of Butt-Kicking",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 2,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": "footgear",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/116 (small).png",
            "nome": "Yuppie Water",
            "descricao": "Use during any combat. Usable once only, +2 to each elf",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 100,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 2}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/118 (small).png",
            "nome": "Singing & Dancing Sword",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 2,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": null,
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/119 (small).png",
            "nome": "Rapier of Unfairness",
            "descricao": "Usable by Elf Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 600,
            "restricao": "elf",
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/120 (small).png",
            "nome": "Really Impressive Title",
            "descricao": "Sem descrição",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 0,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 3}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/121 (small).png",
            "nome": "Flaming Armor",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 2,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": "armor",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/122 (small).png",
            "nome": "Cheese Grater of Peace",
            "descricao": "Usable by Cleric Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 400,
            "restricao": "cleric",
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/124 (small).png",
            "nome": "Nasty-Tasting Sports Drink",
            "descricao": "Sem descrição",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 200,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 2}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/125 (small).png",
            "nome": "Sneaky Bastard Sword",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 2,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/128 (small).png",
            "nome": "Flaming Poison Potion",
            "descricao": "Sem descrição",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 100,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 3}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/129 (small).png",
            "nome": "Broad Sword",
            "descricao": "Females Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 400,
            "restricao": null,
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/130 (small).png",
            "nome": "Bow With Ribbons",
            "descricao": "Usable by Elf Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 4,
            "tamanho": "small",
            "valor": 800,
            "restricao": "elf",
            "usoUnico": false,
            "slot": "2hands",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/133 (small).png",
            "nome": "Rat on a Stick",
            "descricao": "Hey, it's better than nothing!",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 0,
            "restricao": null,
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/134 (small).png",
            "nome": "Eleven-Foot Pole",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 200,
            "restricao": null,
            "usoUnico": false,
            "slot": "2hands",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/135 (small).png",
            "nome": "Freezing Explosive Potion",
            "descricao": "Sem descrição",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 100,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 3}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/138 (small).png",
            "nome": "Pretty Balloons",
            "descricao": "Sem descrição",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 0,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 5}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/140 (small).png",
            "nome": "Staff of Napalm",
            "descricao": "Usable by Wizard Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 5,
            "tamanho": "small",
            "valor": 800,
            "restricao": "wizard",
            "usoUnico": false,
            "slot": "1hand",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/141 (small).png",
            "nome": "Pantyhose of Giant Strength",
            "descricao": "Not usable by Warrior",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 600,
            "restricao": null,
            "usoUnico": false,
            "slot": null,
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/142 (small).png",
            "nome": "Potion of General Studliness",
            "descricao": "Sem descrição",
            "efeito": "levelup",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 0,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 1}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/144 (small).png",
            "nome": "Helm of Courage",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 200,
            "restricao": null,
            "usoUnico": false,
            "slot": "headgear",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/145 (small).png",
            "nome": "Pointy Hat of Power",
            "descricao": "Usable by Wizard Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "small",
            "valor": 400,
            "restricao": "wizard",
            "usoUnico": false,
            "slot": "headgear",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/147 (small).png",
            "nome": "Spiky Knees",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 200,
            "restricao": null,
            "usoUnico": false,
            "slot": null,
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/148 (small).png",
            "nome": "Boil an Anthill",
            "descricao": "Sem descrição",
            "efeito": "levelup",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 0,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 1}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/149 (small).png",
            "nome": "Whine at the GM",
            "descricao": "You can't use this if you are currently the Highest level player or tied.",
            "efeito": "levelup",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 0,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 1}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/150 (small).png",
            "nome": "Huge Rock",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": "big",
            "valor": 0,
            "restricao": null,
            "usoUnico": false,
            "slot": "2hands",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/151 (small).png",
            "nome": "Shield of Ubiquity",
            "descricao": "Usable by Warrior Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 4,
            "tamanho": "big",
            "valor": 600,
            "restricao": "warrior",
            "usoUnico": false,
            "slot": "1hands",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/152 (small).png",
            "nome": "Leather Armor",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 200,
            "restricao": null,
            "usoUnico": false,
            "slot": "armor",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/153 (small).png",
            "nome": "1000 Gold Pieces",
            "descricao": "Sem descrição",
            "efeito": "levelup",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 0,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 1}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/154 (small).png",
            "nome": "Limburger and Anchovy Sandwich",
            "descricao": "Usable by Halfling Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 3,
            "tamanho": null,
            "valor": 400,
            "restricao": "halfling",
            "usoUnico": false,
            "slot": null,
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/155 (small).png",
            "nome": "Horny Helmet",
            "descricao": "Sem descrição",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 1,
            "tamanho": "small",
            "valor": 600,
            "restricao": null,
            "usoUnico": false,
            "slot": "headgear",
            "parameters": null
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/157 (small).png",
            "nome": "Electric Radioactive Acid Potion",
            "descricao": "Sem descrição",
            "efeito": "buff",
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": null,
            "tamanho": null,
            "valor": 200,
            "restricao": null,
            "usoUnico": true,
            "slot": null,
            "parameters": {"valor": 5}
        }
    },
    {
        "type": "item",
        "attributes": {
            "imagepath": "Assets/treasure/158 (small).png",
            "nome": "Cloak of Obscurity",
            "descricao": "Usable by Thief Only",
            "efeito": null,
            "tipo": "item",
            "deckOrigem": "tesouro",
            "poder": 4,
            "tamanho": "small",
            "valor": 600,
            "restricao": "thief",
            "usoUnico": false,
            "slot": null,
            "parameters": null
        }
    }
]
"""

