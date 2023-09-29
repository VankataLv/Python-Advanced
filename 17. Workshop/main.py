def check_valid_player_choice(player_choice: str, board: list) -> bool:
    """The func receives str from current player and check its validity (1-7). Afterwords return a bool."""
    try:
        player_choice = int(player_choice)
        if player_choice in range(1, COLS + 1):
            if board[0][player_choice - 1] == 0:
                return True
            else:
                print("Sorry selected column is full")
        else:
            print("Sorry invalid column! Please pick a number between 1 and 7!")
            return False
    except ValueError:
        print("Sorry invalid choice! Please pick a number between 1 and 7!")


def drop_piece(col_to_drop: int, board: list, player: int) -> tuple:
    """This function executes the drop of the piece on the board"""
    pointer = col_to_drop - 1
    cur_row = 0
    for cur_row in range(len(board)):
        if cur_row == ROWS - 1:
            board[cur_row][pointer] = player
            break
        elif board[cur_row + 1][pointer] != 0:
            board[cur_row][pointer] = player
            break
    coord_last_dropped_piece = (cur_row, pointer)  # row, col
    return board, coord_last_dropped_piece


def check_win_conditions(coord: tuple, board: list, player: int) -> tuple:
    # coord = row, col
    """This func will check if the current player has won"""
    # check horizontal win
    row = coord[0]
    all_possible_indexes_hor = {0: [(0, 1, 2, 3)],
                                1: [(0, 1, 2, 3), (1, 2, 3, 4)],
                                2: [(0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5)],
                                3: [(0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)],
                                4: [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)],
                                5: [(2, 3, 4, 5), (3, 4, 5, 6)],
                                6: [(3, 4, 5, 6)]}
    possible_indexes = all_possible_indexes_hor[coord[1]]
    for el in possible_indexes:
        if board[row][el[0]] == board[row][el[1]] == board[row][el[2]] == board[row][el[3]] == player:
            return True, player
        else:
            continue
    # check vertical win
    all_possible_indexes_ver = {0: [(0, 1, 2, 3)],
                                1: [(0, 1, 2, 3), (1, 2, 3, 4)],
                                2: [(0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5)],
                                3: [(0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5)],
                                4: [(1, 2, 3, 4), (2, 3, 4, 5)],
                                5: [(2, 3, 4, 5)]
                                }
    col = coord[1]
    possible_indexes = all_possible_indexes_ver[row]
    for el in possible_indexes:
        if board[el[0]][col] == board[el[1]][col] == board[el[2]][col] == board[el[3]][col] == player:
            return True, player
        else:
            continue
    # check diagonal win

    return False, player


ROWS, COLS = 6, 7
field = []
cur_player = 1
win_conditions = False
winner = 0
player_choice_col = 0
turn_counter = 0
# Admin row showing col numbers for users
admin_row = [x for x in range(1, 8)]
# Fill the field with zeroes representing empty squares
for _ in range(ROWS):
    field.append([0 for x in range(COLS)])

while not win_conditions:
    print("Here is the gaming board!")
    print(*admin_row, "<- columns")
    [print(*row) for row in field]
    print(f"Player {cur_player}, please choose a column to drop your piece!")
    valid_choice = False
    while not valid_choice:
        player_choice_col = input()
        valid_choice = check_valid_player_choice(player_choice_col, field)
    player_choice_col = int(player_choice_col)
    result = drop_piece(player_choice_col, field, cur_player)
    field, last_piece_coord = result[0], result[1]
    result_win = check_win_conditions(last_piece_coord, field, cur_player)
    win_conditions, winner = result_win[0], result_win[1]
    turn_counter += 1
    if turn_counter == ROWS * COLS and not win_conditions:
        print("DRAW")
        exit()
    if cur_player == 1:
        cur_player = 2
    elif cur_player == 2:
        cur_player = 1
    continue
print(f"---Player {winner} WON!---")
print(*admin_row, "<- columns")
[print(*row) for row in field]
print("-------------------")
