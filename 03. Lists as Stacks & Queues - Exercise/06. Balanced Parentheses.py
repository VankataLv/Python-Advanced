from collections import deque

seq = deque(input())
open_brackets = deque()

while seq:
    cur_bracket = seq.popleft()
    if cur_bracket in "{[(":
        open_brackets.append(cur_bracket)
    elif not open_brackets:
        print("NO")
        break
    else:
        if f"{open_brackets.pop() + cur_bracket}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")


