SIZE = int(input())
racing_num = input()
matrix = []

for _ in range(SIZE):
    matrix.append([x for x in input().split()])

car_coords = {"row": 0, "col": 0}
distance_travelled = 0
directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

while True:
    cmd = input()
    if cmd == "End":
        print(f"Racing car {racing_num} DNF.")
        break
    else:
        if matrix[car_coords["row"] + directions[cmd][0]][car_coords["col"] + directions[cmd][1]] == ".":
            car_coords["row"] += directions[cmd][0]
            car_coords["col"] += directions[cmd][1]
            distance_travelled += 10
        elif matrix[car_coords["row"] + directions[cmd][0]][car_coords["col"] + directions[cmd][1]] == "T":
            car_coords["row"] += directions[cmd][0]
            car_coords["col"] += directions[cmd][1]
            for row_i_tunnel in range(SIZE):
                for col_i_tunnel in range(SIZE):
                    if matrix[row_i_tunnel][col_i_tunnel] == "T":
                        if row_i_tunnel == car_coords["row"] and col_i_tunnel == car_coords["col"]:
                            continue
                        else:
                            matrix[car_coords["row"]][car_coords["col"]] = "."
                            car_coords["row"] = row_i_tunnel
                            car_coords["col"] = col_i_tunnel
                            distance_travelled += 30
                            matrix[car_coords["row"]][car_coords["col"]] = "."
        elif matrix[car_coords["row"] + directions[cmd][0]][car_coords["col"] + directions[cmd][1]] == "F":
            distance_travelled += 10
            print(f"Racing car {racing_num} finished the stage!")
            car_coords["row"] += directions[cmd][0]
            car_coords["col"] += directions[cmd][1]
            break

matrix[car_coords["row"]][car_coords["col"]] = "C"
print(f"Distance covered {distance_travelled} km.")
[print("".join(row)) for row in matrix]
