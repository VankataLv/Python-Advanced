from collections import deque

tools = deque([int(el) for el in input().split()])
substances = [int(el) for el in input().split()]
challenges = [int(el) for el in input().split()]

while tools and substances and challenges:
    cur_tool = tools.popleft()
    cur_substance = substances.pop()
    result = cur_tool * cur_substance
    if result in challenges:
        challenges.remove(result)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break
    else:
        cur_tool += 1
        tools.append(cur_tool)
        cur_substance -= 1
        if cur_substance != 0:
            substances.append(cur_substance)

    if not tools or not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    tools = [str(el) for el in tools]
    print(f"Tools: {', '.join(tools)}")
if substances:
    substances = [str(el) for el in substances]
    print(f"Substances: {', '.join(substances)}")
if challenges:
    challenges = [str(el) for el in challenges]
    print(f"Challenges: {', '.join(challenges)}")
