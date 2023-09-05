rows, columns = [int(el) for el in input().split(", ")]
my_matrix = []

for _ in range(rows):
    inner_list = []
    cur_row_data = [int(el) for el in input().split(", ")]
    for el in cur_row_data:
        inner_list.append(el)
    my_matrix.append(inner_list)
total_sum = 0
for el in my_matrix:
    total_sum += sum(el)
print(total_sum)
print(my_matrix)
