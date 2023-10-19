from collections import deque

monsters = deque([int(el) for el in input().split(",")])
soldiers = [int(el) for el in input().split(",")]
monsters_killed = 0

while monsters and soldiers:
    cur_monster = monsters.popleft()
    cur_soldier = soldiers.pop()

    if cur_soldier >= cur_monster:
        cur_soldier -= cur_monster
        monsters_killed += 1
        if cur_soldier > 0:
            if soldiers:
                soldiers[-1] += cur_soldier
            else:
                soldiers.append(cur_soldier)
    else:
        cur_monster -= cur_soldier
        monsters.append(cur_monster)

if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
