rows = int(input())
matrix = []
for _ in range(rows):
    inner_lst = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(inner_lst)
print(matrix)

print([[int(el) for el in input().split(", ") if int(el) % 2 == 0]for row in range(int(input()))])
