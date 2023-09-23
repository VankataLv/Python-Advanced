def concatenate(*args, **kwargs):
    print(args)
    print(kwargs)
    final_str = ""
    for el in args:
        final_str += el
    for el in kwargs:
        if el in final_str:
            final_str = final_str.replace(el, kwargs[el])
    return final_str


# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))