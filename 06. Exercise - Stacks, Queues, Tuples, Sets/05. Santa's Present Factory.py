from collections import deque

ready_for_christmas = False
box_materials = deque(int(el) for el in input().split())
magic_levels = deque(int(el) for el in input().split())
ready_presents_db = {}
magic_needed = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
                }

while len(box_materials) > 0 and len(magic_levels) > 0:
    cur_magic_level = box_materials[-1] * magic_levels[0]
    if cur_magic_level in magic_needed.keys():
        if magic_needed[cur_magic_level] in ready_presents_db:
            ready_presents_db[magic_needed[cur_magic_level]] += 1
        else:
            ready_presents_db[magic_needed[cur_magic_level]] = 1
        box_materials.pop()
        magic_levels.popleft()
        if "Doll" in ready_presents_db.keys() and "Train" in ready_presents_db.keys():
            ready_for_christmas = True
        if "Teddy bear" in ready_presents_db.keys() and "Bicycle" in ready_presents_db.keys():
            ready_for_christmas = True
    elif cur_magic_level < 0:
        box_materials.append(box_materials.pop() + magic_levels.popleft())
    elif cur_magic_level > 0:
        magic_levels.popleft()
        box_materials[-1] += 15
    else:
        if box_materials[-1] == 0:
            box_materials.pop()
        if magic_levels[0] == 0:
            magic_levels.popleft()

if ready_for_christmas:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if box_materials:
    print(f"Materials left: {', '.join([str(el) for el in box_materials][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(el) for el in magic_levels])}")

my_keys_sorted = list(ready_presents_db.keys())
my_keys_sorted.sort()
for sorted_key in my_keys_sorted:
    print(f"{sorted_key}: {ready_presents_db[sorted_key]}")
