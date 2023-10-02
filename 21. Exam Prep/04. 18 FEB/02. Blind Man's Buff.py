ROWS, COLS = [int(value) for value in input().split()]
playground = []
for _ in range(ROWS):
    playground.append([el for el in input().split()])

cur_pos = {}
for i_row in range(ROWS):
    for i_col in range(COLS):
        if playground[i_row][i_col] == "B":
            cur_pos = {"row": i_row, "col": i_col}

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}
valid_rows = range(0, ROWS)
valid_cols = range(0, COLS)
score = 0
moves = 0
command = ""
while score < 3:
    command = input()
    if command == "Finish":
        break
    if cur_pos["row"] + directions[command][0] in valid_rows and\
       cur_pos["col"] + directions[command][1] in valid_cols:
        if playground[cur_pos["row"] + directions[command][0]][cur_pos["col"] + directions[command][1]] == "O":
            continue
        elif playground[cur_pos["row"] + directions[command][0]][cur_pos["col"] + directions[command][1]] == "-":
            playground[cur_pos["row"]][cur_pos["col"]] = "-"
            cur_pos["row"] += directions[command][0]
            cur_pos["col"] += directions[command][1]
            moves += 1
            playground[cur_pos["row"]][cur_pos["col"]] = "B" # Just for clarity during debug
        elif playground[cur_pos["row"] + directions[command][0]][cur_pos["col"] + directions[command][1]] == "P":
            playground[cur_pos["row"]][cur_pos["col"]] = "-"
            cur_pos["row"] += directions[command][0]
            cur_pos["col"] += directions[command][1]
            score += 1
            moves += 1
            playground[cur_pos["row"]][cur_pos["col"]] = "B"  # Just for clarity during debug

print("Game over!")
print(f"Touched opponents: {score} Moves made: {moves}")
# [print(row) for row in playground] # For debug purposes
