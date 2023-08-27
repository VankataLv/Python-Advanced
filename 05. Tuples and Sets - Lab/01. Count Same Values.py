my_tup = tuple([float(num) for num in input().split()])
unique_nums_count = {}

for el in my_tup:
    if el not in unique_nums_count:
        unique_nums_count[el] = 0
    unique_nums_count[el] += 1

for key, value in unique_nums_count.items():
    print(f"{key:.1f} - {value} times")

