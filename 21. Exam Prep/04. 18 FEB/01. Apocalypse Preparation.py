# 50 / 100 Judge
from collections import deque

textiles = deque([int(el) for el in input().split()])
medicines = [int(el) for el in input().split()]
items_created = {}

while len(textiles) > 0 and len(medicines) > 0:
    cur_textile = textiles.popleft()
    cur_medicine = medicines.pop()
    summed_products = cur_textile + cur_medicine
    if summed_products == 30:
        if "Patch" not in items_created:
            items_created["Patch"] = 1
        else:
            items_created["Patch"] += 1
    elif summed_products == 40:
        if "Bandage" not in items_created:
            items_created["Bandage"] = 1
        else:
            items_created["Bandage"] += 1
    elif summed_products == 100:
        if "MedKit" not in items_created:
            items_created["MedKit"] = 1
        else:
            items_created["MedKit"] += 1
    else:
        if summed_products > 100:
            summed_products -= 100
            if "MedKit" not in items_created:
                items_created["MedKit"] = 1
            else:
                items_created["MedKit"] += 1
            medicines[-1] += summed_products
        else:
            cur_medicine += 10
            medicines.append(cur_medicine)

if not textiles and not medicines:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicines:
    print("Medicaments are empty.")

items_created = sorted(items_created.items(), key=lambda x: (-x[1], x[0]))
for item in items_created:
    print(f"{item[0]} - {item[1]}")

if medicines:
    medicines.sort(reverse=True)
    medicines = [str(el) for el in medicines]
    print(f'Medicaments left: {", ".join(medicines)}')
if textiles:
    textiles = list(textiles)
    textiles.sort(reverse=True)
    textiles = [str(el) for el in textiles]
    print(f'Textiles left: {", ".join(textiles)}')
