from collections import deque

q = deque()

cmd = input()
while cmd != "End":
    if cmd == "Paid":
        for customer in range(len(q)):
            print(q.popleft())
        q.clear()
    else:
        q.append(cmd)
    cmd = input()
print(f"{len(q)} people remaining.")

