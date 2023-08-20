from collections import deque

qty_food = int(input())

orders = input(). split(" ")
orders = deque([int(el) for el in orders])
print(max(orders))
for order in orders.copy():
    if order <= qty_food:
        qty_food -= order
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str (el) for el in orders])}")
        break

if not orders:
    print("Orders complete")
