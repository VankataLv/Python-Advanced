collected_hazelnuts = 0
SIZE = int(input())
cmds = [x for x in input().split(", ")]

field = []
for _ in range(SIZE):
    field.append(list(input()))

cur_pos = {}
for row_i in range(SIZE):
    for col_i in range(SIZE):
        if field[row_i][col_i] == "s":
            cur_pos["row"] = row_i
            cur_pos["col"] = col_i
            break

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

additional_msg = True
valid_i = [int(el) for el in range(0, SIZE)]
for cur_cmd in cmds:
    if cur_pos["row"] + directions[cur_cmd][0] not in valid_i or \
       cur_pos["col"] + directions[cur_cmd][1] not in valid_i:
        print("The squirrel is out of the field.")
        additional_msg = False
        break
    else:
        field[cur_pos["row"]][cur_pos["col"]] = "*"
        cur_pos["row"] += directions[cur_cmd][0]
        cur_pos["col"] += directions[cur_cmd][1]
        if field[cur_pos["row"]][cur_pos["col"]] == "*":
            continue
        elif field[cur_pos["row"]][cur_pos["col"]] == "h":
            field[cur_pos["row"]][cur_pos["col"]] = "*"
            collected_hazelnuts += 1
            if collected_hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                additional_msg = False
                break
        elif field[cur_pos["row"]][cur_pos["col"]] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            additional_msg = False
            break

if additional_msg:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")
