my_stack = []

n = int(input())

for i in range(n):
    cmd = input()
    if cmd == "2":
        if my_stack:
            my_stack.pop()
    elif cmd == "3":
        if my_stack:
            print(max(my_stack))
    elif cmd == "4":
        if my_stack:
            print(min(my_stack))
    elif cmd[0] == "1":
        action, num_to_add = cmd.split(" ")
        num_to_add = int(num_to_add)
        my_stack.append(num_to_add)

my_stack.reverse()
print(*my_stack, sep=", ")
