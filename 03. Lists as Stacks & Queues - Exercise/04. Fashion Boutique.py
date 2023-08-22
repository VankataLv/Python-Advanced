from collections import deque

box = deque([int(outfit) for outfit in input().split()])
rack_cap_default = int(input())
racks_used = 1
cur_rack_cap = rack_cap_default

while box:
    cur_outfit = box.pop()
    if cur_rack_cap >= cur_outfit:
        cur_rack_cap -= cur_outfit
    else:
        racks_used += 1
        cur_rack_cap = rack_cap_default
        cur_rack_cap -= cur_outfit

print(racks_used)
