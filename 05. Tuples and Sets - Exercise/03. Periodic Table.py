n = int(input())
per_table = set()
lst_of_data = []
for _ in range(n):
    lst_of_data = input().split()
    for el in lst_of_data:
        per_table.add(el)
for unique_el in per_table:
    print(unique_el)
