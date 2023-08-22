from collections import deque

total_pumps = int(input())
circle_road = deque()
fuel_left = 0
for pump_num in range(total_pumps):
    amount_gas, distance_next = input().split()
    circle_road.append([int(amount_gas), int(distance_next)])

