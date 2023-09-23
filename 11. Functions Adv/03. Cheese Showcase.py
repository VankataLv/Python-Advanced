def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for (cheese_name, quantities) in sorted_data:
        result.append(cheese_name)
        sorted_qtys_lst = sorted(quantities, reverse=True)
        result += sorted_qtys_lst

    return "\n".join([str(el) for el in result])
print(sorting_cheeses(
    Parmesan=[102, 120, 135],
    Camembert=[100, 100, 105, 500, 430],
    Mozzarella=[50, 125],))
