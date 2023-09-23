def even_odd(*args):
    lst_nums = list(args)
    cmd = lst_nums.pop()
    if cmd == "even":
        lst_for_return = [int(x) for x in lst_nums if x % 2 == 0]
    else:
        lst_for_return = [int(x) for x in lst_nums if x % 2 != 0]
    return lst_for_return

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))