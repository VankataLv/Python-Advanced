matrix = []
for _ in range(5):
    matrix.append([el for el in input().split()])

cur_player_pos = {"row": 0, "col": 0}
tgts_coords = []
tgts_hit = []
for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            cur_player_pos = {"row": row, "col": col}  # this is only the initial pos
        elif matrix[row][col] == "x":
            tgts_coords.append([row, col])

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}  # represents one square movement in the key direction

for _ in range(int(input())):
    action, *data = input().split(" ")
    if action == "move":
        direction, steps = data[0], int(data[1])
        if cur_player_pos["row"] + (directions[direction][0] * steps) in range(0, 5) and \
                cur_player_pos["col"] + (directions[direction][1] * steps) in range(0, 5):
            no_targets_in_path = True
            for step in range(1, steps + 1):
                if matrix[cur_player_pos["row"] + directions[direction][0] * step]\
                         [cur_player_pos["col"] + directions[direction][1] * step] == ".":
                    continue
                else:
                    # print("Invalid path -> X")  # DEBUG only!
                    no_targets_in_path = False
                    break
            if no_targets_in_path:
                matrix[cur_player_pos["row"]][cur_player_pos["col"]] = "."
                cur_player_pos["row"] += (directions[direction][0] * steps)
                cur_player_pos["col"] += (directions[direction][1] * steps)
                matrix[cur_player_pos["row"]][cur_player_pos["col"]] = "A"
        else:
            # print("Out of range")  # DEBUG only!
            continue

    elif action == "shoot":
        dir_shot = data[0]
        if dir_shot == "up":
            for sqr in range(cur_player_pos["row"] - 1, 0, -1):
                if matrix[sqr][cur_player_pos["col"]] == "x":
                    matrix[sqr][cur_player_pos["col"]] = "."
                    tgts_coords.remove([sqr, [cur_player_pos["col"]]])
                    tgts_hit.append([sqr, cur_player_pos["col"]])
                    break
        elif dir_shot == "down":
            for sqr in range(cur_player_pos["row"] + 1, 5):
                if matrix[sqr][cur_player_pos["col"]] == "x":
                    matrix[sqr][cur_player_pos["col"]] = "."
                    tgts_coords.remove([sqr, cur_player_pos["col"]])
                    tgts_hit.append([sqr, cur_player_pos["col"]])
                    break
        elif dir_shot == "left":
            for sqr in range(cur_player_pos["col"] - 1, 0, -1):
                if matrix[cur_player_pos["row"]][sqr] == "x":
                    matrix[cur_player_pos["row"]][sqr] = "."
                    tgts_coords.remove([cur_player_pos["row"], sqr])
                    tgts_hit.append([cur_player_pos["row"], sqr])
                    break
        elif dir_shot == "right":
            for sqr in range(cur_player_pos["col"] + 1, 5):
                if matrix[cur_player_pos["row"]][sqr] == "x":
                    matrix[cur_player_pos["row"]][sqr] = "."
                    tgts_coords.remove([cur_player_pos["row"], sqr])
                    tgts_hit.append([cur_player_pos["row"], sqr])
                    break

[print(*row) for row in matrix] # for DEBUG only!
if tgts_coords:
    print(f"Training not completed! {len(tgts_coords)} targets left.")
else:
    print(f"Training completed! All {len(tgts_hit)} targets hit.")
[print(tgt) for tgt in tgts_hit]

# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move up 4
# shoot left