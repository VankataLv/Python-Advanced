def check_validity(r, c, mat):
    if r in range(0, len(mat)) and c in range(0, len(mat[0])):
        return True
    else:
        return False


rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split()])
cmd = input()
while cmd != "END":
    cmd = cmd.split()
    action, row, col, value = cmd[0], int(cmd[1]), int(cmd[2]), int(cmd[3])
    if check_validity(row, col, matrix):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    cmd = input()
[print(*row) for row in matrix]
