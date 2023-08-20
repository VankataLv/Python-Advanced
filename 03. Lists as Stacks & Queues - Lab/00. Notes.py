# my_stack = [5, 6, 7, 8, 10, 11]
#
# while len(my_stack) > 1:
#     removed_element = my_stack.pop()
#     print(removed_element)

# First problem
# sentence = input()
# stack_sentence = list(sentence)
# # print(sentence[::-1])
# while stack_sentence:
#     print(stack_sentence.pop(), end="")

# Problem 5
from collections import deque

kids = deque(input().split(" "))

counter = int(input())
print(kids)
