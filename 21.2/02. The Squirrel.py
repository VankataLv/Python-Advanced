SIZE = int(input())
cmds = list(input().split(", "))
collected_nuts = 0
matrix = []

for _ in range(SIZE):
    matrix.append(list(input()))

squirrel_pos = {}

for row_i in range(SIZE):
    for col_i in range(SIZE):
        if matrix[row_i][col_i] == "s":
            squirrel_pos = {"row": row_i,
                            "col": col_i}
            break

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}
turn = 0
for cmd in cmds:
    turn += 1
    squirrel_pos["row"] += directions[cmd][0]
    squirrel_pos["col"] += directions[cmd][1]
    if squirrel_pos["row"] not in range(0, SIZE):
        print("The squirrel is out of the field.")
        break
    elif squirrel_pos["col"] not in range(0, SIZE):
        print("The squirrel is out of the field.")
        break

    else:
        if matrix[squirrel_pos["row"]][squirrel_pos["col"]] == "h":
            collected_nuts += 1
            if collected_nuts == 3:
                print("Good job! You have collected all hazelnuts!")
                break
        elif matrix[squirrel_pos["row"]][squirrel_pos["col"]] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break

    if turn == len(cmds):
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_nuts}")
