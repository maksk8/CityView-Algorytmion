import random

#creating 5x5 matrix "sudoku" like
def place_numbers(board, row, col):
    if row == 5 and col == 5:
        return True
    if row == 5:
        row = 0
        col += 1
    if col == 5:
        return True
    for num in vector:
        if check_valid(board, row, col, num):
            board[row][col] = num
            if place_numbers(board, row+1, col):
                return True
            board[row][col] = 0
    return False

def check_valid(board, row, col, num):
    for i in range(5):
        if board[i][col] == num or board[row][i] == num:
            return False
    return True

#generating 2d arr
board = [[0 for i in range(5)] for j in range(5)]

with open("dane.txt", "r") as f:
    line = f.readline().strip()
    vector = list(map(int, line.split(" ")))


#randVector = random.sample(range(1, 6), 5)

place_numbers(board, 0, 0)


#creating arrays of viewers from each side
left = []
right = []
up = []
down = []

#from left
for i in range(5):
    max = 0
    counter = 0
    for j in range(5):
        if board[i][j] > max:
            max = board[i][j]
            counter += 1

    left.append(counter)

#from right
for i in range(5):
    max = 0
    counter = 0
    for j in range(5):
        if board[i][4 - j] > max:
            max = board[i][4 - j]
            counter += 1

    right.append(counter)

#from up
for i in range(5):
    max = 0
    counter = 0
    for j in range(5):
        if board[j][i] > max:
            max = board[j][i]
            counter += 1

    up.append(counter)

#from down
for i in range(5):
    max = 0
    counter = 0
    for j in range(5):
        if board[4 - j][i] > max:
            max = board[4 - j][i]
            counter += 1

    down.append(counter)


#assembling final view in output file

with open("output.txt", "w") as file:
    file.write("# ")
    for item in up:
        file.write(str(item) + " ")
    file.write("#\n")

    for i in range(5):
        file.write(str(left[i]) + " ")
        for item in board[i]:
            file.write(str(item) + " ")
        file.write(str(right[i]) + "\n")

    file.write("# ")
    for item in down:
        file.write(str(item) + " ")
    file.write("#\n")

#output in console

print("#", end=" ")
for item in up:
    print(item, end=" ")
print("#")

for i in range(5):
    print(left[i], end=" ")
    for item in board[i]:
        print(item, end=" ")
    print(right[i])

print("#", end=" ")
for item in down:
    print(item, end=" ")
print("#")














