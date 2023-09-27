r, c = [int(el) for el in input().split()]
matrix = []
for row in range(r):
    cur_row = []
    for col in range(c):
        # cur_el = []
        cur_el = chr(row + 97) + chr(row + 97 + col) + chr(row + 97)
        cur_row.append(cur_el)
    matrix.append(cur_row)
[print(*row) for row in matrix]
