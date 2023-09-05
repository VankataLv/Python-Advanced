size = int(input())
matrix = [[int(el) for el in input().split()] for row in range(size)]
primary_diagonal_sum = 0
for i in range(size):
    primary_diagonal_sum += matrix[i][i]
print(primary_diagonal_sum)

