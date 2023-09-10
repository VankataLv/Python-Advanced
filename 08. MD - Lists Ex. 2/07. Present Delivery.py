presents = int(input())
size = int(input())
matrix = []
for _ in range(size):
    matrix.append(input().split())

santa_pos = {"row": 0, "col": 0}
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            santa_pos = {"row": row, "col": col}

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}  # represents one square movement in the key direction
count_nice_kids_with_presents = 0
cmd = input()
while cmd != "Christmas morning":
    if 0 <= santa_pos["row"] + directions[cmd][0] < size and \
            0 <= santa_pos["col"] + directions[cmd][1] < size:
        matrix[santa_pos["row"]][santa_pos["col"]] = "-"
        santa_pos["row"] += directions[cmd][0]
        santa_pos["col"] += directions[cmd][1]
        if matrix[santa_pos["row"]][santa_pos["col"]] == "X":
            matrix[santa_pos["row"]][santa_pos["col"]] = "-"
        elif matrix[santa_pos["row"]][santa_pos["col"]] == "V":
            matrix[santa_pos["row"]][santa_pos["col"]] = "-"
            presents -= 1
            count_nice_kids_with_presents += 1
            if presents < 1:
                break
        elif matrix[santa_pos["row"]][santa_pos["col"]] == "C":
            matrix[santa_pos["row"]][santa_pos["col"]] = "-"
            for direction in directions:
                if matrix[santa_pos["row"] + directions[direction][0]][santa_pos["col"] + directions[direction][1]] == "V":
                    count_nice_kids_with_presents += 1
                    matrix[santa_pos["row"] + directions[direction][0]][santa_pos["col"] + directions[direction][1]] = "-"
                    presents -= 1
                    if presents < 1:
                        break
                elif matrix[santa_pos["row"] + directions[direction][0]][santa_pos["col"] + directions[direction][1]] == "X":
                    matrix[santa_pos["row"] + directions[direction][0]][santa_pos["col"] + directions[direction][1]] = "-"
                    presents -= 1
                    if presents < 1:
                        break
        matrix[santa_pos["row"]][santa_pos["col"]] = "S"
    if presents < 1:
        break
    cmd = input()
if presents < 1:
    for row in matrix:
        if "V" in row:
            print("Santa ran out of presents!")
[print(*row) for row in matrix]
kids_no_presents = 0
for el in matrix:
    if "V" in el:
        kids_no_presents += 1
if kids_no_presents:
    print(f"No presents for {kids_no_presents} nice kid/s.")
else:
    print(f"Good job, Santa! {count_nice_kids_with_presents} happy nice kid/s.")

# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning