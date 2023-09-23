def grocery_store(**kwargs):

    result = dict(sorted(kwargs.items(), key=lambda x: kwargs[x]))
    print(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))