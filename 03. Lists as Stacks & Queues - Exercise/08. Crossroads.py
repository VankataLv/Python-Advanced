from collections import deque

green_light = int(input())
window = int(input())
q_cars_waiting = deque()
cur_time = 0
crash = False
total_cars_passed = 0
cur_passing_car = deque()
while True:
    cmd = input()
    if cmd == "green":
        while q_cars_waiting:
            cur_passing_whole_car = (q_cars_waiting.popleft())
            for char in cur_passing_whole_car:
                cur_passing_car.append(char)
            while cur_passing_car:
                ....


    elif cmd == "End":
        break
    else:                          # cmd is a car
        q_cars_waiting.append(cmd)

if not crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
