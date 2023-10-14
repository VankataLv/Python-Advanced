# Judge 40/100
def coord_converter(r: int, c: int) -> str:
    rows_nums = [str(el) for el in range(8, -1, -1)]
    col_letters = [chr(value) for value in range(97, 105)]
    coords_to_return = ""
    coords_to_return += col_letters[c]
    coords_to_return += rows_nums[r]
    return coords_to_return


board = []
pos_white = {}
pos_black = {}
for _ in range(8):
    board.append([el for el in input().split()])

for row_i in range(8):
    for col_i in range(8):
        if board[row_i][col_i] == "w":
            pos_white = {"row": row_i, "col": col_i}
        elif board[row_i][col_i] == "b":
            pos_black = {"row": row_i, "col": col_i}

queen_conditions = False
capture_conditions = False
current_color = "white"
while not queen_conditions and not capture_conditions:
    if current_color == "white":
        try:
            if board[pos_white["row"] - 1][pos_white["col"] - 1] == "b" or \
                    board[pos_white["row"] - 1][pos_white["col"] + 1] == "b":
                capture_conditions = True
                print(f"Game over! White win, capture on {coord_converter(pos_black['row'], pos_black['col'])}.")
        except IndexError:
            pass
        else:
            pos_white["row"] -= 1
            if pos_white["row"] == 0:
                queen_conditions = True
                print(
                    f"Game over! White pawn is promoted to a queen at {coord_converter(pos_white['row'], pos_white['col'])}.")
    if current_color == "black":
        try:
            if board[pos_black["row"] + 1][pos_black["col"] - 1] == "w" or \
                    board[pos_black["row"] + 1][pos_black["col"] + 1] == "w":
                capture_conditions = True
                print(f"Game over! Black win, capture on {coord_converter(pos_white['row'], pos_white['col'])}.")
        except IndexError:
            pass
        else:
            pos_black["row"] += 1
            if pos_black["row"] == 7:
                queen_conditions = True
                print(
                    f"Game over! Black pawn is promoted to a queen at {coord_converter(pos_black['row'], pos_black['col'])}.")
    if current_color == "white":
        current_color = "black"
    else:
        current_color = "white"

