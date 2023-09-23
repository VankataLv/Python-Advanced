def even_odd_filter(**kwargs):
    working_dict = dict(kwargs)
    for el in working_dict:
        if el == "odd":
            working_dict["odd"] = [x for x in working_dict["odd"] if x % 2 != 0]
        elif el == "even":
            working_dict["even"] = [x for x in working_dict["even"] if x % 2 == 0]
    return dict(sorted(working_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
