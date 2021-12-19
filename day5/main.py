from os import cpu_count
import numpy as np

with open('input.txt') as f:
    wejscie = []
    for line in f.readlines():
        line = line.replace(" -> ", ",")
        line = line.rstrip("\n")
        line = line.split(",")
        numbers = [int(num) for num in line]
        wejscie.append(numbers)

    ### for large input
    board = [[0 for x in range(1000)] for y in range(1000)]

    ### for small input
    # board = [[0 for x in range(10)] for y in range(10)]

    for coordinate in wejscie:
        x1 = min(coordinate[0], coordinate[2])
        x2 = max(coordinate[0], coordinate[2])
        y1 = min(coordinate[1], coordinate[3])
        y2 = max(coordinate[1], coordinate[3])

        ### part 1 filling verticals and horizontals
        if x1 == x2:
            for y in range(y1, y2 + 1):
                board[y][x1] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                board[y1][x] += 1

        ### part 2 filling diagonals 
        elif abs(coordinate[0] - coordinate[2]) == abs(coordinate[1] - coordinate[3]):      ### check slope 
            if coordinate[0] > coordinate[2] and coordinate[1] < coordinate[3]:
                x = coordinate[0]
                y = coordinate[1]

                while x >= coordinate[2]:
                    board[y][x] += 1
                    x -= 1
                    y += 1

            elif coordinate[0] > coordinate[2] and coordinate[1] > coordinate[3]:
                x = coordinate[0]
                y = coordinate[1]

                while x >= coordinate[2]:
                    board[y][x] += 1
                    x -= 1
                    y -= 1

            elif coordinate[0] < coordinate[2] and coordinate[1] < coordinate[3]:
                x = coordinate[0]
                y = coordinate[1]

                while x <= coordinate[2]:
                    board[y][x] += 1
                    x += 1
                    y += 1
            
            elif coordinate[0] < coordinate[2] and coordinate[1] > coordinate[3]:
                x = coordinate[0]
                y = coordinate[1]

                while x <= coordinate[2]:
                    board[y][x] += 1
                    x += 1
                    y -= 1

    counter = 0
    for line in board:
        for i in line:
            if i > 1:
                counter += 1

    print(counter) 


