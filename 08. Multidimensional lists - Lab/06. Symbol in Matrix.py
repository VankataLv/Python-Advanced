size = int(input())
matrix = [[el for el in input()] for row in range(size)]
special_symbol = input()
coordinates = None
for i in range(size):
    if coordinates:
        break
    for j in range(size):
        if matrix[i][j] == special_symbol:
            coordinates = f"({i}, {j})"
            break

if coordinates:
    print(coordinates)
else:
    print(f"{special_symbol} does not occur in the matrix")
