# 92/100 Judge
from collections import deque

chocolates = input().split(", ")    # stack LIFO
chocolates = deque([int(x) for x in chocolates])
cups_milk = input().split(", ")   # queue FIFO
cups_milk = deque([int(x) for x in cups_milk])
milkshakes = 0

while milkshakes < 5 and len(chocolates) > 0 and len(cups_milk) > 0:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_milk[0] <= 0:
        cups_milk.popleft()
        continue
    if chocolates[-1] == cups_milk[0]:
        chocolates.pop()
        cups_milk.popleft()
        milkshakes += 1
    else:
        chocolates[-1] -= 5
        cups_milk.append(cups_milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
else:
    print("Chocolate: empty")
if cups_milk:
    print(f"Milk: {', '.join([str(el) for el in cups_milk])}")
else:
    print("Milk: empty")

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55

# -10, -2, -30, 10
# -5

# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6