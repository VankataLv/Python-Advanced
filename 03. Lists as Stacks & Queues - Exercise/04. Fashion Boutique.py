box = input().split(" ")
box = [int(el) for el in box]
cap_for_rack = int(input())
racks_used = 0
cap_current_rack = cap_for_rack
cur_outfit = 0
while box:
    if cap_current_rack >= cur_outfit:
        cap_current_rack -= cur_outfit
        cur_outfit = box.pop()
    else:
        racks_used += 1
        cap_current_rack = cap_for_rack
print(racks_used)
