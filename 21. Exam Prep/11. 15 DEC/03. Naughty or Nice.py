def naughty_or_nice_list(*santa_list, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []
    kids_tup, cmds = santa_list[0], santa_list[1:]
    for cmd in cmds:
        num, behavior = cmd.split("-")
        num = int(num)
        counter = 0
        for kid_tup in kids_tup:
            if num == kid_tup[0]:
                counter += 1
        if counter == 1:
            for kid_tup in kids_tup:
                if num == kid_tup[0]:
                    if behavior == "Nice":
                        nice_list.append(kid_tup[1])
                        kids_tup.remove(kid_tup)
                    elif behavior == "Naughty":
                        naughty_list.append(kid_tup[1])
                        kids_tup.remove(kid_tup)

    for cmd in kwargs.items():
        name, behavior = cmd[0], cmd[1]
        counter = 0
        for kid_tup in kids_tup:
            if name == kid_tup[1]:
                counter += 1
        if counter == 1:
            for kid_tup in kids_tup:
                if name == kid_tup[1]:
                    if behavior == "Nice":
                        nice_list.append(kid_tup[1])
                        kids_tup.remove(kid_tup)
                    elif behavior == "Naughty":
                        naughty_list.append(kid_tup[1])
                        kids_tup.remove(kid_tup)

    if kids_tup:
        for left_kids in kids_tup:
            not_found_list.append(left_kids[1])

    result = ""
    if nice_list:
        result += f"Nice: {', '.join(nice_list)}\n"
    if naughty_list:
        result += f"Naughty: {', '.join(naughty_list)}\n"
    if not_found_list:
        result += f"Not found: {', '.join(not_found_list)}\n"

    return result

# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
