def grocery_store(**kwargs):
    working_dict = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0] ))
    result = []
    for el in working_dict:
        result.append(f"{el[0]}: {el[1]}")
    return "\n".join([str(el) for el in result])


# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
