# solution 66/100
ROWS, COLS = [int(el) for el in input().split()]
end_program_conditions = False

neighbourhood = []
for _ in range(ROWS):
    neighbourhood.append(list(input()))

initial_position = {}

for i_row in range(ROWS):
    for i_col in range(COLS):
        if neighbourhood[i_row][i_col] == "B":
            initial_position["row"] = i_row
            initial_position["col"] = i_col
            break

cur_position = initial_position.copy()  # {"row":int, "col": int}
while not end_program_conditions:
    cmd = input()
    if cmd == "up":
        if cur_position["row"] - 1 not in range(0, ROWS):
            end_program_conditions = True
            print("The delivery is late. Order is canceled.")
            neighbourhood[initial_position["row"]][initial_position["col"]] = " "
        else:
            if neighbourhood[cur_position["row"] - 1][cur_position["col"]] == "*":
                continue
            elif neighbourhood[cur_position["row"] - 1][cur_position["col"]] == "P":
                cur_position["row"] -= 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "R"
                print("Pizza is collected. 10 minutes for delivery.")
            elif neighbourhood[cur_position["row"] - 1][cur_position["col"]] == "-":
                cur_position["row"] -= 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "."
            elif neighbourhood[cur_position["row"] - 1][cur_position["col"]] == "A":
                cur_position["row"] -= 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "P"
                print("Pizza is delivered on time! Next order...")
                end_program_conditions = True
    elif cmd == "down":
        if cur_position["row"] + 1 not in range(0, ROWS):
            end_program_conditions = True
            print("The delivery is late. Order is canceled.")
            neighbourhood[initial_position["row"]][initial_position["col"]] = " "
        else:
            if neighbourhood[cur_position["row"] + 1][cur_position["col"]] == "*":
                continue
            elif neighbourhood[cur_position["row"] + 1][cur_position["col"]] == "P":
                cur_position["row"] += 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "R"
                print("Pizza is collected. 10 minutes for delivery.")
            elif neighbourhood[cur_position["row"] + 1][cur_position["col"]] == "-":
                cur_position["row"] += 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "."
            elif neighbourhood[cur_position["row"] + 1][cur_position["col"]] == "A":
                cur_position["row"] += 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "P"
                print("Pizza is delivered on time! Next order...")
                end_program_conditions = True
    elif cmd == "left":
        if cur_position["col"] - 1 not in range(0, COLS):
            end_program_conditions = True
            print("The delivery is late. Order is canceled.")
            neighbourhood[initial_position["row"]][initial_position["col"]] = " "
        else:
            if neighbourhood[cur_position["row"]][cur_position["col"] - 1] == "*":
                continue
            elif neighbourhood[cur_position["row"]][cur_position["col"] - 1] == "P":
                cur_position["col"] -= 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "R"
                print("Pizza is collected. 10 minutes for delivery.")
            elif neighbourhood[cur_position["row"]][cur_position["col"] - 1] == "-":
                cur_position["col"] -= 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "."
            elif neighbourhood[cur_position["row"]][cur_position["col"] - 1] == "A":
                cur_position["col"] -= 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "P"
                print("Pizza is delivered on time! Next order...")
                end_program_conditions = True
    elif cmd == "right":
        if cur_position["col"] + 1 not in range(0, COLS):
            end_program_conditions = True
            print("The delivery is late. Order is canceled.")
            neighbourhood[initial_position["row"]][initial_position["col"]] = " "
        else:
            if neighbourhood[cur_position["row"]][cur_position["col"] + 1] == "*":
                continue
            elif neighbourhood[cur_position["row"]][cur_position["col"] + 1] == "P":
                cur_position["col"] += 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "R"
                print("Pizza is collected. 10 minutes for delivery.")
            elif neighbourhood[cur_position["row"]][cur_position["col"] + 1] == "-":
                cur_position["col"] += 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "."
            elif neighbourhood[cur_position["row"]][cur_position["col"] + 1] == "A":
                cur_position["col"] += 1
                neighbourhood[cur_position["row"]][cur_position["col"]] = "P"
                print("Pizza is delivered on time! Next order...")
                end_program_conditions = True

for row in neighbourhood:
    print("".join(row))

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# right
# right
# right
# right
# up
# up
# up

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# left
# right
# right
# right
# right
# right
# up
