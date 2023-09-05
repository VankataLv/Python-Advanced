matrix = [[int(el) for el in input().split(", ")]for row in range(int(input()))]
flatten = []
for el in matrix:
    flatten.extend(el)
print(flatten)

# flatten = [el for lst_el in matrix for el in lst_el]
# print(flatten)