from cardstack import CardStack

meu_deck = CardStack()

# meu_deck.push("A")
# meu_deck.push("2")
# meu_deck.push("3")
# meu_deck.push("4")
# meu_deck.push("5")
# meu_deck.push("Z")

print(f"Tamanho: {meu_deck.getSize()}")

meu_deck.push_wherever("x")

print(f"Tamanho: {meu_deck.getSize()}")
print(f"POP: {meu_deck.pop()}")
# print(f"POP: {meu_deck.pop()}")
