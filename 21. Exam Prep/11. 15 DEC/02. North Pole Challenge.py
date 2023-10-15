def add_colectables(r, c, board):
    global gifts_counter
    global cookies_counter
    global decorations_counter
    global collected_stuff
    if board[r][c] == "D":
        decorations_counter -= 1
        collected_stuff["decorations"] += 1
    elif board[r][c] == "G":
        gifts_counter -= 1
        collected_stuff["gifts"] += 1
    elif board[r][c] == "C":
        cookies_counter -= 1
        collected_stuff["cookies"] += 1


ROWS, COLS = input().split(", ")
ROWS = int(ROWS)
COLS = int(COLS)
matrix = []
for _ in range(ROWS):
    matrix.append(input().split())

cur_pos = {}
decorations_counter = 0
gifts_counter = 0
cookies_counter = 0
collected_stuff = {"decorations": 0, "gifts": 0, "cookies": 0}
for row_i in range(ROWS):
    for col_i in range(COLS):
        if matrix[row_i][col_i] == "Y":
            cur_pos["row"] = row_i
            cur_pos["col"] = col_i
        elif matrix[row_i][col_i] == "D":
            decorations_counter += 1
        elif matrix[row_i][col_i] == "G":
            gifts_counter += 1
        elif matrix[row_i][col_i] == "C":
            cookies_counter += 1

collected_all = False
cmd = input()
while cmd != "End" and not collected_all:
    direction, steps = cmd.split("-")
    steps = int(steps)
    for step in range(steps):
        matrix[cur_pos["row"]][cur_pos["col"]] = "x"
        if direction == "up":
            cur_pos["row"] -= 1
            if cur_pos["row"] < 0:
                cur_pos["row"] = ROWS - 1
            add_colectables(cur_pos["row"], cur_pos["col"], matrix)
        elif direction == "down":
            cur_pos["row"] += 1
            if cur_pos["row"] > ROWS - 1:
                cur_pos["row"] = 0
            add_colectables(cur_pos["row"], cur_pos["col"], matrix)
        elif direction == "left":
            cur_pos["col"] -= 1
            if cur_pos["col"] < 0:
                cur_pos["col"] = COLS - 1
            add_colectables(cur_pos["row"], cur_pos["col"], matrix)
        elif direction == "right":
            cur_pos["col"] += 1
            if cur_pos["col"] > COLS - 1:
                cur_pos["col"] = 0
            add_colectables(cur_pos["row"], cur_pos["col"], matrix)
        matrix[cur_pos["row"]][cur_pos["col"]] = "Y"
        if decorations_counter == 0 and gifts_counter == 0 and cookies_counter == 0:
            collected_all = True
            break
    if collected_all:
        break
    else:
        cmd = input()

if decorations_counter == 0 and gifts_counter == 0 and cookies_counter == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_stuff['decorations']} Christmas decorations")
print(f"- {collected_stuff['gifts']} Gifts")
print(f"- {collected_stuff['cookies']} Cookies")
[print(' '.join(row)) for row in matrix]
