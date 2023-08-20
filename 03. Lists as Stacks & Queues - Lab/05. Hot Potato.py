from collections import deque

players = deque(input().split(" "))
n = int(input())
counter = 1

while len(players) > 1:
    player = players.popleft()
    if counter == n:
        print(f"Removed {player}")
        counter = 1
    else:
        counter += 1
        players.append(player)

winner = players.popleft()
print(f"Last is {winner}")

