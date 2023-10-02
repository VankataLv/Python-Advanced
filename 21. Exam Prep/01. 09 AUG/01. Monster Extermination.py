from collections import deque

monster_armors = deque([int(x) for x in input().split(",")])
soldier_strikes = [int(x) for x in input().split(",")]
killed_monsters = 0
while len(monster_armors) > 0 and len(soldier_strikes) > 0:
    cur_monster = monster_armors.popleft()
    cur_soldier = soldier_strikes.pop()
    if cur_soldier >= cur_monster:  # soldier is stronger
        cur_soldier -= cur_monster
        killed_monsters += 1
        if cur_soldier > 0:
            if len(soldier_strikes) > 0:
                soldier_strikes[-1] += cur_soldier
            else:
                soldier_strikes.append(cur_soldier)
    else:                           # monster is stronger
        cur_monster -= cur_soldier
        monster_armors.append(cur_monster)

if len(monster_armors) == 0:
    print("All monsters have been killed!")
if len(soldier_strikes) == 0:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
