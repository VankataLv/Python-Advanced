from collections import deque
area = []
for _ in range(6):
    area.append(input().split())

cmds = deque([el for el in input().split(", ")])
water_found, metal_found, concrete_found = False, False, False

cur_pos = {}
for row_i in range(6):
    for col_i in range(6):
        if area[row_i][col_i] == "E":
            cur_pos["row"] = row_i
            cur_pos["col"] = col_i
            break

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}
while cmds:
    cur_cmd = cmds.popleft()
    if cur_pos["row"] + directions[cur_cmd][0] > 5:
        cur_pos["row"] = 0
        cur_pos["col"] += directions[cur_cmd][1]
    elif cur_pos["row"] + directions[cur_cmd][0] < 0:
        cur_pos["row"] = 5
        cur_pos["col"] += directions[cur_cmd][1]
    elif cur_pos["col"] + directions[cur_cmd][1] > 5:
        cur_pos["row"] += directions[cur_cmd][0]
        cur_pos["col"] = 0
    elif cur_pos["col"] + directions[cur_cmd][1] < 0:
        cur_pos["row"] += directions[cur_cmd][0]
        cur_pos["col"] = 5
    else:
        cur_pos["row"] += directions[cur_cmd][0]
        cur_pos["col"] += directions[cur_cmd][1]

    if area[cur_pos["row"]][cur_pos["col"]] == "R":
        print(f"Rover got broken at ({cur_pos['row']}, {cur_pos['col']})")
        break
    elif area[cur_pos["row"]][cur_pos["col"]] == "W":
        print(f"Water deposit found at ({cur_pos['row']}, {cur_pos['col']})")
        water_found = True
    elif area[cur_pos["row"]][cur_pos["col"]] == "M":
        print(f"Metal deposit found at ({cur_pos['row']}, {cur_pos['col']})")
        metal_found = True
    elif area[cur_pos["row"]][cur_pos["col"]] == "C":
        print(f"Concrete deposit found at ({cur_pos['row']}, {cur_pos['col']})")
        concrete_found = True

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
