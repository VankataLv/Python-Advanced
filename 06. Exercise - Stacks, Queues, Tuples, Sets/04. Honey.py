from collections import deque

honey_made = 0
bees = input().split()
bees = deque([int(el) for el in bees]) # FIFO
nectar = input().split()
nectar = deque([int(el) for el in nectar])  #LIFO
process = input().split()
process = deque([el for el in process])

while len(bees) > 0 and len(nectar) > 0:
    if nectar[-1] >= bees[0]:
        if process[0] == "+":
            honey_made += abs(bees.popleft() + nectar.pop())
        elif process[0] == "-":
            honey_made += abs(bees.popleft() - nectar.pop())
        elif process[0] == "*":
            honey_made += abs(bees.popleft() * nectar.pop())
        elif process[0] == "/":
            if nectar.pop() == 0:
                nectar.pop()
                bees.popleft()
            honey_made += abs(bees.popleft() / nectar.pop())
        process.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(el) for el in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(el) for el in nectar])}")
