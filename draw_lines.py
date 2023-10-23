"""Draw lines with pico"""


# motor manual control delay (milliseconds)
MTR_DELAY = 2

# signals read by pico
Y_UP = "1"
X_LEFT = "2"
Y_DOWN = "3"
X_RIGHT = "4"
Z_RAISE = "5"
Z_LOWER = "6"

SCALE = 2
X_START = 0
Y_START = 0

# matrix = [[0, 0, 0, 0, 0, 0],
#           [0, 0, 1, 1, 0, 0],
#           [0, 1, 0, 0, 1, 0],
#           [0, 1, 0, 0, 1, 0],
#           [0, 0, 1, 1, 0, 0],
#           [0, 0, 0, 0, 0, 0]]

# matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
#           [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#           [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# MATRIX = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
#           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
#           [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#           [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
#           [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
#           [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

MATRIX = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# MATRIX = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# x = X_START
# y = Y_START
# for row in matrix:
#     y += 1
#     x = 0  # restart x counter
#     for value in row:
#         x += 1
#         if value == 1:
#             print(x, y)

# x = X_START
# y = Y_START
# for row in matrix:
#     y += 1
#     x = 0  # restart x counter
#     for value in row:
#         x += 1
#         if value == 1:
#             matrix[y-1][x-1] = 0
#             print(x, y)


def main():
    position = [0, 0]
    print("RAISE")
    # while there still "1"s in the matrix
    while check(MATRIX):
        # find first "1" in matrix

        x = -1
        y = -1
        exit_loop = 0
        for row in MATRIX:
            y += 1
            x = -1  # restart x counter
            for value in row:
                x += 1
                if value == 1:
                    print(position)
                    give_instructions(position, x, y)
                    position = [x + 1, y + 1]
                    print("LOWER")
                    # print(x + 1, y + 1)
                    MATRIX[y][x] = 2
                    exit_loop = 1
                    break
            if exit_loop == 1:
                break
        # print("loop exited")

        # go to next "1" in clockwise direction if there is one closeby
        while True:

            # 0  0  0
            # 0 "1" 1
            # 0  0  0  => right
            if MATRIX[y][x + 1] == 1:
                x += 1

            # 0  0  0
            # 0 "1" 0
            # 0  0  1  => bottom right
            elif MATRIX[y + 1][x + 1] == 1:
                y += 1
                x += 1

            # 0  0  0
            # 0 "1" 0
            # 0  1  0  => bottom
            elif MATRIX[y + 1][x] == 1:
                y += 1

            # 0  0  0
            # 0 "1" 0
            # 1  0  0  => bottom left
            elif MATRIX[y + 1][x - 1] == 1:
                y += 1
                x += -1

            # 0  0  0
            # 1 "1" 0
            # 0  0  0  => left
            elif MATRIX[y][x - 1] == 1:
                x += -1

            # 1  0  0
            # 0 "1" 0
            # 0  0  0  => top left
            elif MATRIX[y - 1][x - 1] == 1:
                y += -1
                x += -1

            # 0  1  0
            # 0 "1" 0
            # 0  0  0  => top
            elif MATRIX[y - 1][x] == 1:
                y += -1

            # 0  0  1
            # 0 "1" 0
            # 0  0  0  => top right
            elif MATRIX[y - 1][x + 1] == 1:
                y += -1
                x += 1

            else:
                break

            give_instructions(position, x, y)
            position = [x + 1, y + 1]
            # print(x + 1, y + 1)
            MATRIX[y][x] = 2
        print("RAISE")
    # print matrix
    for row in MATRIX:
        print(row)


def check(matrix):
    """Check if matrix contains "1" """
    for row in matrix:
        for value in row:
            if value == 1:
                return True
    return False


def give_instructions(position, x, y):
    """Send instructions to pico"""
    while position[0] > x + 1:
        for i in range(SCALE):
            print("MOVE LEFT")
        position[0] += -1
    while position[0] < x + 1:
        for i in range(SCALE):
            print("MOVE RIGHT")
        position[0] += 1
    while position[1] > y + 1:
        for i in range(SCALE):
            print("MOVE UP")
        position[1] += -1
    while position[1] < y + 1:
        for i in range(SCALE):
            print("MOVE DOWN")
        position[1] += 1
    # print(position)


main()
