SIZE = int(input())
directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}
battlefield = []
for _ in range(SIZE):
    battlefield.append(list(input()))
cur_position = {}
sub_health_left = 3
cruisers_left = 3
for row_i in range(SIZE):
    for col_i in range(SIZE):
        if battlefield[row_i][col_i] == "S":
            cur_position = {"row": row_i, "col": col_i}
            break

while sub_health_left > 0 and cruisers_left > 0:
    cmd = input()
    battlefield[cur_position["row"]][cur_position["col"]] = "-"
    if battlefield[cur_position["row"] + directions[cmd][0]][cur_position["col"] + directions[cmd][1]] == "-":
        cur_position["row"] += directions[cmd][0]
        cur_position["col"] += directions[cmd][1]
    elif battlefield[cur_position["row"] + directions[cmd][0]][cur_position["col"] + directions[cmd][1]] == "*":
        cur_position["row"] += directions[cmd][0]
        cur_position["col"] += directions[cmd][1]
        sub_health_left -= 1
        if sub_health_left == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{cur_position['row']}, {cur_position['col']}]!")
    elif battlefield[cur_position["row"] + directions[cmd][0]][cur_position["col"] + directions[cmd][1]] == "C":
        cur_position["row"] += directions[cmd][0]
        cur_position["col"] += directions[cmd][1]
        cruisers_left -= 1
        if cruisers_left == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    battlefield[cur_position["row"]][cur_position["col"]] = "S"

[print("".join(row)) for row in battlefield]
