# Zadanie 1 - lista zakupów, słownik i kapitalizacja
shopping_dict = {
  "piekarnia": ["chleb", "pączek", "bułki"],
  "warzywniak": ["marchew", "seler", "rukola"]
}

i = 0
print("Lista zakupów:")

for shop, products in shopping_dict.items():
    print(f"Idę do {shop.capitalize()} i kupuję tam: "
      f"{', '.join([product.capitalize() for product in products])}.")
    for product in products:
        i += 1

print(f"W sumie kupuję {i} produktów")