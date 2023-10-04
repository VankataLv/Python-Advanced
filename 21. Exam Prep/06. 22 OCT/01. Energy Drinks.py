from collections import deque

mils_caffeine = [int(x) for x in input().split(",")]
energy_drinks = deque([int(x) for x in input().split(",")])
stamat_caffeine = 0

while mils_caffeine and energy_drinks:
    cur_caffeine = mils_caffeine.pop()
    cur_drink = energy_drinks.popleft()
    cur_product = cur_caffeine * cur_drink
    if cur_product + stamat_caffeine < 300:
        stamat_caffeine += cur_product
    else:
        energy_drinks.append(cur_drink)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0

if energy_drinks:
    energy_drinks = [str(x) for x in energy_drinks]
    print(f"Drinks left: {', '.join(energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")