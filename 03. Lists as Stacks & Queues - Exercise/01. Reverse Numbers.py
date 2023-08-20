# 3 solutions

stack = input().split(" ")
while stack:
    print(stack.pop(), end=" ")

from collections import deque

q = deque(input().split())

for _ in range(len(q)):
    print(q.pop(), end=" ")     # why pop() not popleft()?

from collections import deque
numbers = deque(input().split())
numbers.reverse()

print(' '.join(numbers))