biggest_sum = 0
biggest_sum_values = []
max_rows, max_columns = [int(el) for el in input().split(", ")]
matrix = []

cur_sum_values = []
for _ in range(max_rows):
    matrix.append([int(el) for el in input().split(', ')])

for row_ind in range(max_rows - 1): # 0, 1, 2
    for col_ind in range(max_columns): # 0, 1, 2, 3, 4, 5
        cur_sum_values = []
        cur_sum_values.append(matrix[row_ind][col_ind])
        if col_ind == max_columns - 1:
            break
        cur_sum_values.append(matrix[row_ind][col_ind + 1])
        for j in range(2):
            cur_sum_values.append(matrix[row_ind + 1][col_ind + j])
        if sum(cur_sum_values) > biggest_sum:
            biggest_sum = sum(cur_sum_values)
            biggest_sum_values = cur_sum_values # may not work try copy
    if row_ind == max_rows - 1:
        break

print(f'{biggest_sum_values[0]} {biggest_sum_values[1]} ')
print(f'{biggest_sum_values[2]} {biggest_sum_values[3]} ')
print(biggest_sum)
