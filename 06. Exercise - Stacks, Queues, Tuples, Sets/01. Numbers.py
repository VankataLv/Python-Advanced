first = set(int(num) for num in input().split())
second = set(int(num) for num in input().split())
n = int(input())
for _ in range(n):
    cmd, place, *data = input().split()
    if cmd == "Add":
        if place == "First":
            [first.add(int(el)) for el in data]
        elif place == "Second":
            [second.add(int(el)) for el in data]
    elif cmd == "Remove":
        if place == "First":
            [first.discard(int(el)) for el in data]
        elif place == "Second":
            [second.discard(int(el)) for el in data]
    elif cmd == "Check":
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")

