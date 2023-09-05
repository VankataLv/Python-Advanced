rows, columns = [int(qty) for qty in input().split(", ")]
matrix = []
for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

for j in range(columns):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(col_sum)
