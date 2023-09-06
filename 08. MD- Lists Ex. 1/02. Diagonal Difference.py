size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(size)]
primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][size - 1 - i] for i in range(size)]
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

# 4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14