# Judge 76/100
from collections import deque

elf_energies = deque([int(el) for el in input().split()])
materials_in_box = [int(el) for el in input().split()]
counter = 0
toys_made = 0
total_energy_used = 0
while elf_energies and materials_in_box:
    cur_elf = elf_energies.popleft()
    while cur_elf < 5:
        if not elf_energies:
            break
        else:
            cur_elf = elf_energies.popleft()
    cur_box = materials_in_box.pop()
    counter += 1
    if counter % 3 == 0 and counter % 5 == 0:
        if cur_elf >= cur_box * 2:
            total_energy_used += cur_box * 2
            cur_elf -= cur_box * 2
            elf_energies.append(cur_elf)
        else:
            cur_elf *= 2
            materials_in_box.append(cur_box)
            elf_energies.append(cur_elf)
    elif counter % 3 == 0:
        if cur_elf >= cur_box * 2:
            total_energy_used += cur_box * 2
            cur_elf -= cur_box * 2
            toys_made += 2
            cur_elf += 1
            elf_energies.append(cur_elf)
        else:
            cur_elf *= 2
            materials_in_box.append(cur_box)
            elf_energies.append(cur_elf)
    elif counter % 5 == 0:
        if cur_elf >= cur_box:
            total_energy_used += cur_box
            cur_elf -= cur_box
            elf_energies.append(cur_elf)
        else:
            cur_elf *= 2
            materials_in_box.append(cur_box)
            elf_energies.append(cur_elf)
    else:
        if cur_elf >= cur_box:
            total_energy_used += cur_box
            cur_elf -= cur_box
            cur_elf += 1
            toys_made += 1
        else:
            cur_elf *= 2
            materials_in_box.append(cur_box)
        elf_energies.append(cur_elf)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy_used}")
if elf_energies:
    elf_energies = [str(el) for el in elf_energies]
    print(f"Elves left: {', '.join(elf_energies)}")
if materials_in_box:
    materials_in_box = [str(el) for el in materials_in_box]
    print(f"Boxes left: {', '.join(materials_in_box)}")
