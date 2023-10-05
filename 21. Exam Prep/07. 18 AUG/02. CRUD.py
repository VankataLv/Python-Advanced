matrix = []
for _ in range(6):
    matrix.append(input().split())

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

init_pos = input()
cur_pos = {"row": int(init_pos[1]),
           "col": int(init_pos[4])}

line = input()
while line != "Stop":
    cmd, *info = line.split(", ")
    cur_pos["row"] += directions[info[0]][0]
    cur_pos["col"] += directions[info[0]][1]
    if cmd == "Create":
        if matrix[cur_pos["row"]][cur_pos["col"]] == ".":
            matrix[cur_pos["row"]][cur_pos["col"]] = info[1]
    elif cmd == "Update":
        if matrix[cur_pos["row"]][cur_pos["col"]] != ".":
            matrix[cur_pos["row"]][cur_pos["col"]] = info[1]
    elif cmd == "Delete":
        if matrix[cur_pos["row"]][cur_pos["col"]] != ".":
            matrix[cur_pos["row"]][cur_pos["col"]] = "."
    elif cmd == "Read":
        if matrix[cur_pos["row"]][cur_pos["col"]] != ".":
            print(matrix[cur_pos["row"]][cur_pos["col"]])
    line = input()

[print(" ".join(row)) for row in matrix]