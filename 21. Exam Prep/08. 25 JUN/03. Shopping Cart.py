def shopping_cart(*products):
    db = {"Soup": [],
          "Pizza": [],
          "Dessert": []}

    for product in products:
        if product == "Stop":
            break
        else:
            if product[0] == "Soup":
                if len(db["Soup"]) == 3:
                    pass
                else:
                    if product[1] not in db["Soup"]:
                        db["Soup"].append(product[1])
            elif product[0] == "Pizza":
                if len(db["Pizza"]) == 4:
                    pass
                else:
                    if product[1] not in db["Pizza"]:
                        db["Pizza"].append(product[1])
            elif product[0] == "Dessert":
                if len(db["Dessert"]) == 2:
                    pass
                else:
                    if product[1] not in db["Dessert"]:
                        db["Dessert"].append(product[1])

    result = ""
    if len(db["Soup"]) == 0 and len(db["Pizza"]) == 0 and len(db["Dessert"]) == 0:
        result = "No products in the cart!"
    else:
        for meal in db.items():
            meal[1].sort()

        db = dict(sorted(db.items(), key=lambda x: (-len(x[1]), x[0])))

        for k, v in db.items():
            result += f"{k}:\n"
            for prod in v:
                result += f" - {prod}\n"
    return result

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))