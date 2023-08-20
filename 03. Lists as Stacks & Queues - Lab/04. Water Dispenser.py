from collections import deque

q = deque()
water_left = int(input())
people = input()
while people != "Start":
    q.append(people)
    people = input()
cmd = input()
while cmd != "End":
    line_args = cmd.split(" ")
    if len(line_args) == 1:
        if int(cmd) <= water_left:
            water_left -= int(cmd)
            print(f"{q.popleft()} got water")
        else:
            print(f"{q.popleft()} must wait")
    else:
        liters_to_refill = int(line_args[1])
        water_left += liters_to_refill
    cmd = input()
print(f"{water_left} liters left")
