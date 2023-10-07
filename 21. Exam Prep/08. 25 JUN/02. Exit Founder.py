# Judge 85/100
from collections import deque
first_player, second_player = input().split(", ")
maze =[]
for _ in range(6):
    maze.append([el for el in input().split()])

cur_player = first_player
next_player = deque([first_player, second_player])

while True:
    coordinates = input()
    cur_row = int(coordinates[1])
    cur_col = int(coordinates[4])
    cur_player = next_player.popleft()
    if cur_player == "MISS":
        continue
    if maze[cur_row][cur_col] == "E":
        print(f"{cur_player} found the Exit and wins the game!")
        break
    elif maze[cur_row][cur_col] == "T":
        if cur_player == first_player:
            print(f"{first_player} is out of the game! The winner is {second_player}.")
        else:
            print(f"{second_player} is out of the game! The winner is {first_player}.")
        break
    elif maze[cur_row][cur_col] == "W":
        print(f"{cur_player} hits a wall and needs to rest.")
        next_player.append("MISS")
        if cur_player == first_player:
            next_player.append(second_player)
        else:
            next_player.append(first_player)
    next_player.append(cur_player)



