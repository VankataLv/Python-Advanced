from collections import deque

total_pumps = int(input())
circle_road = deque()
fuel_left = 0

for pump_num in range(total_pumps):
    amount_gas, distance_next = input().split()
    circle_road.append([int(amount_gas), int(distance_next)])

for index in range(total_pumps):
    copy_circle_road = circle_road.copy()
    while copy_circle_road:
        cur_pump_data = copy_circle_road.popleft()
        fuel_left += cur_pump_data[0]
        if fuel_left >= cur_pump_data[1]:
            fuel_left -= cur_pump_data[1]
            continue
        else:
            fuel_left = 0
            circle_road.rotate(-1)
            break
    else:
        print(index)
        break
