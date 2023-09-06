biggest_sum = 0
biggest_sum_val_matrix = []
rows, columns = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
for row in range(rows - 2):   # 0, 1
    for col in range(columns - 2):  # 0, 1, 2
        cur_matrix_val = []
        cur_sum = 0
        for i in range(3):
            cur_matrix_val.append([])
            for j in range(3):
                cur_matrix_val[i].append(matrix[row + i][col + j])
            cur_sum += sum(cur_matrix_val[i])
        if cur_sum > biggest_sum:
            biggest_sum = cur_sum
            biggest_sum_val_matrix = cur_matrix_val
print(f"Sum = {biggest_sum}")
# print(f"{' '.join(str(el) for el in biggest_sum_val_matrix)}")
[print(*row) for row in biggest_sum_val_matrix]
