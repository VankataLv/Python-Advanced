def accommodate_new_pets(availlable_cap: int, max_weight_limit: float, *args):
    accommodated_pets = {}
    args = list(args)
    pets_waiting = len(args)
    while availlable_cap > 0 and pets_waiting > 0:
        for pet in args:
            if availlable_cap == 0:
                break
            pets_waiting -= 1
            if pet[1] <= max_weight_limit:
                availlable_cap -= 1
                if pet[0] in accommodated_pets:
                    accommodated_pets[pet[0]] += 1
                else:
                    accommodated_pets[pet[0]] = 1
            else:                                   # weight of pet exceeds hotel weight limit
                continue
    result = []
    if pets_waiting == 0 and availlable_cap > 0:
        result.append(f"All pets are accommodated! Available capacity: {availlable_cap}.")
    elif pets_waiting > 0:
        result.append(f"You did not manage to accommodate all pets!")
    result.append("Accommodated pets:")
    accommodated_pets = sorted(accommodated_pets.items(), key=lambda x: (x[0], x[1]))
    result.append([f"{x[0]}: {x[1]}" for x in accommodated_pets])
    return [el for el in result]

# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))
# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))