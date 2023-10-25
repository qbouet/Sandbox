import math
FILE_NAME = "matrix.text"

matrix = []
for row in range(40):
    column = []
    for number in range(45):
        column.append(0)
    matrix.append(column)

for row in matrix:
    print(row)

print("\n\n")

x = 0
y = 0
for i in range(43):
    try:
        x += 1
        y = int(-5*math.sin(0.5*x)) + 20
        # print(x, math.sin(0.1*x))
        matrix[y][x] = 1

    except IndexError:
        break

for row in matrix:
    print(row)

out_file = open(FILE_NAME, 'w')
for row in matrix:
    print(row, file=out_file)
out_file.close()
