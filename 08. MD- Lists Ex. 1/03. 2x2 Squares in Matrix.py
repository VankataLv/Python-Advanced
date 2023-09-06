rows, columns = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]
total_identical_matrix = 0
cur_matrix_val = set()
for row in range(rows - 1):   # 0, 1, 2
    for col in range(columns - 1):  # 0, 1, 2, 3
        cur_matrix_val.clear()
        cur_matrix_val = set(matrix[row][col])
        cur_matrix_val.add(matrix[row][col + 1])
        for i in range(2):
            cur_matrix_val.add(matrix[row + 1][col + i])
        if len(cur_matrix_val) == 1:
            total_identical_matrix += 1
print(total_identical_matrix)

# 3 4
# A B B D
# E B B B
# I J B B
