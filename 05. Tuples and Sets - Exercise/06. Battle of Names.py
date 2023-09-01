rows = int(input())
odd = set()
even = set()
for row in range(1, rows + 1):
    name = input()
    cur_value = 0
    for char in name:
        cur_value += ord(char)
    cur_value //= row
    if cur_value % 2 == 0:
        even.add(cur_value)
    else:
        odd.add(cur_value)
odd_sum = sum(odd)
even_sum = sum(even)
if odd_sum > even_sum:
    z = odd.symmetric_difference_update(even)
    print(f'{", ".join([str(el) for el in z])}')
elif odd_sum < even_sum:
    z = odd.symmetric_difference(even)
    print(f'{", ".join([str(el) for el in z])}')
else:
    print(f'{odd}')