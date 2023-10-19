from collections import deque

materials = [int(el) for el in input().split()]
magics = deque([int(el) for el in input().split()])

gemstone_made = False
sculpture_made = False
gold_made = False
jewellery_made = False

while materials and magics:
    cur_mat = materials.pop()
    cur_magic = magics.popleft()
    summed_mat_magic = cur_mat + cur_magic
    if summed_mat_magic in range(100, 200):
        pass
    elif summed_mat_magic in range(200, 300):
        pass
    elif summed_mat_magic in range(300, 400):
        pass
    elif summed_mat_magic in range(400, 500):
        pass
    else:
        if summed_mat_magic < 100:
            pass
        elif summed_mat_magic > 100:
            pass
