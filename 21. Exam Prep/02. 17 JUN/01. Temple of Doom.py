from collections import deque
tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]
end_conditions = False

while not end_conditions:
    cur_tool = tools.popleft()
    cur_substance = substances.pop()
    product = cur_tool * cur_substance
    if product in challenges:
        challenges.remove(product)
    else:
        cur_tool += 1
        tools.append(cur_tool)
        cur_substance -= 1
        if cur_substance > 0:
            substances.append(cur_substance)
    if len(tools) == 0 or len(substances) == 0:
        if len(challenges) > 0:
            print("Harry is lost in the temple. Oblivion awaits him.")
            break
    if len(challenges) == 0:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
