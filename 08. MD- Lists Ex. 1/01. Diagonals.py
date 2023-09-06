size = int(input())
matrix = [[int(el) for el in input().split(", ")]for row in range(size)]
primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][size - 1 - i] for i in range(size)]
print(f'Primary diagonal: {", ".join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
