# 85/100
ROWS, COLS = [int(x) for x in input().split(",")]
cupboard_area = []
for _ in range(ROWS):
    cupboard_area.append(list(input()))

cur_position = {}
cheese_left = 0
for i_row in range(ROWS):
    for i_col in range(COLS):
        if cupboard_area[i_row][i_col] == "M":
            cur_position["row"] = i_row
            cur_position["col"] = i_col
        elif cupboard_area[i_row][i_col] == "C":
            cheese_left += 1

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

while cheese_left > 0:
    command = input()
    if command == "danger":
        if cheese_left > 0:
            print("Mouse will come back later!")

    elif command in directions:
        if cur_position["row"] + directions[command][0] not in range(0, ROWS) or\
           cur_position["col"] + directions[command][1] not in range(0, COLS):
            print("No more cheese for tonight!")
            break

        else:
            if cupboard_area[cur_position["row"] + directions[command][0]]\
                            [cur_position["col"] + directions[command][1]] == "T":
                print("Mouse is trapped!")
                cupboard_area[cur_position["row"]][cur_position["col"]] = "*"
                cupboard_area[cur_position["row"] + directions[command][0]]\
                             [cur_position["col"] + directions[command][1]] = "M"
                break

            elif cupboard_area[cur_position["row"] + directions[command][0]]\
                              [cur_position["col"] + directions[command][1]] == "C":
                cupboard_area[cur_position["row"]][cur_position["col"]] = "*"
                cur_position["row"] += directions[command][0]
                cur_position["col"] += directions[command][1]
                cupboard_area[cur_position["row"]][cur_position["col"]] = "M"
                cheese_left -= 1
                if cheese_left == 0:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break

            elif cupboard_area[cur_position["row"] + directions[command][0]]\
                              [cur_position["col"] + directions[command][1]] == "*":
                cupboard_area[cur_position["row"]][cur_position["col"]] = "*"
                cur_position["row"] += directions[command][0]
                cur_position["col"] += directions[command][1]
                cupboard_area[cur_position["row"]][cur_position["col"]] = "M"

            elif cupboard_area[cur_position["row"] + directions[command][0]]\
                              [cur_position["col"] + directions[command][1]] == "@":
                continue

[print("".join(row)) for row in cupboard_area]
