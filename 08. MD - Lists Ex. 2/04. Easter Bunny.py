def up(mat, bunny):
    cur_coord_row = bunny[0]
    cur_eggs = 0
    coord_moved = []
    while 0 <= cur_coord_row - 1 < size:
        cur_coord_row -= 1
        if mat[cur_coord_row][bunny[1]] != "X":
            cur_eggs += mat[cur_coord_row][bunny[1]]
            coord_moved.append([cur_coord_row, bunny[1]])
        else:
            break
    return cur_eggs, coord_moved


def down(mat, bunny):
    cur_coord_row = bunny[0]
    cur_eggs = 0
    coord_moved = []
    while 0 <= cur_coord_row + 1 < size:
        cur_coord_row += 1
        if mat[cur_coord_row][bunny[1]] != "X":
            cur_eggs += mat[cur_coord_row][bunny[1]]
            coord_moved.append([cur_coord_row, bunny[1]])
        else:
            break
    return cur_eggs, coord_moved


def right(mat, bunny):
    cur_coord_col = bunny[1]
    cur_eggs = 0
    coord_moved = []
    while 0 <= cur_coord_col + 1 < size:
        cur_coord_col += 1
        if mat[bunny[0]][cur_coord_col] != "X":
            cur_eggs += mat[bunny[0]][cur_coord_col]
            coord_moved.append([bunny[0], cur_coord_col])
        else:
            break
    return cur_eggs, coord_moved


def left(mat, bunny):
    cur_coord_col = bunny[1]
    cur_eggs = 0
    coord_moved = []
    while 0 <= cur_coord_col - 1 < size:
        cur_coord_col -= 1
        if mat[bunny[0]][cur_coord_col] != "X":
            cur_eggs += mat[bunny[0]][cur_coord_col]
            coord_moved.append([bunny[0], cur_coord_col])
        else:
            break
    return cur_eggs, coord_moved


size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(el) if el.isdigit() else el for el in input().split()])

bunny_coords = ()
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_coords = (row, col)

direction_db = {"up": up(matrix, bunny_coords), "down": down(matrix, bunny_coords), "left": left(matrix, bunny_coords),
                "right": right(matrix, bunny_coords)}

best_direction = max(direction_db, key=direction_db.get)
print(best_direction)
for el in direction_db[best_direction][1]:
    print(el)
print(direction_db[best_direction][0])

# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22