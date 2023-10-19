ROWS, COLS = input().split(",")
ROWS = int(ROWS)
COLS = int(COLS)
matrix = []

for _ in range(ROWS):
    matrix.append(list(input()))

mouse_pos = {}
cheese_left = 0
for row_i in range(ROWS):
    for col_i in range(COLS):
        if matrix[row_i][col_i] == "M":
            mouse_pos["row"] = row_i
            mouse_pos["col"] = col_i
        elif matrix[row_i][col_i] == "C":
            cheese_left += 1

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

cmd = input()
while True:
    if cmd == "danger":
        if cheese_left:
            print("Mouse will come back later!")
            break
    if mouse_pos["row"] + directions[cmd][0] in range(ROWS) and mouse_pos["col"] + directions[cmd][1] in range(COLS):
        if matrix[mouse_pos["row"] + directions[cmd][0]][mouse_pos["col"] + directions[cmd][1]] == "@":
            cmd = input()
            continue
        else:
            matrix[mouse_pos["row"]][mouse_pos["col"]] = "*"
            mouse_pos["row"] += directions[cmd][0]
            mouse_pos["col"] += directions[cmd][1]
            if matrix[mouse_pos["row"]][mouse_pos["col"]] == "C":
                cheese_left -= 1
                matrix[mouse_pos["row"]][mouse_pos["col"]] = "M"
                if cheese_left == 0:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
            elif matrix[mouse_pos["row"]][mouse_pos["col"]] == "T":
                matrix[mouse_pos["row"]][mouse_pos["col"]] = "M"
                print("Mouse is trapped!")
                break
            else:
                matrix[mouse_pos["row"]][mouse_pos["col"]] = "M"

            cmd = input()

    else:
        print("No more cheese for tonight!")
        break

[print("".join(row)) for row in matrix]
