with open("day11_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

matrix = [[int(a) for a in line.strip()] for line in raw_input]
n_column = len(matrix[0])
n_row = len(matrix)

eight_neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
number_of_flashes = 0

def flash_neighbors(y, x):
    for delta_y, delta_x in eight_neighbors:
        y2 = y + delta_y
        x2 = x + delta_x
        if not is_valid(y2, x2):
            continue
        matrix[y2][x2] += 1
        if matrix[y2][x2] == 10:
            flash_neighbors(y2, x2)

def each_turn():
    global number_of_flashes, matrix
    number_of_flash_this_turn = 0
    for i_row in range(n_row):
        for i_column in range(n_column):
            matrix[i_row][i_column] += 1
            if matrix[i_row][i_column] == 10:
                flash_neighbors(i_row, i_column)
    for i_row in range(n_row):
        for i_column in range(n_column):
            if matrix[i_row][i_column] >= 10:
                matrix[i_row][i_column] = 0
                number_of_flash_this_turn += 1
    number_of_flashes += number_of_flash_this_turn
    return number_of_flash_this_turn

def is_valid(y, x):
    if y < 0 or x < 0:
        return False
    if y >= n_row or x >= n_column:
        return False
    return True

for i in range(10000):
    number_of_flashES_this_turn = each_turn()
    if number_of_flashES_this_turn == 100:
        print(i + 1)
        break

