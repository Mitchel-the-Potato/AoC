from time import sleep

with open("day25_input.txt", "r") as f:
    raw_input = [[c for c in line.strip()] for line in f.readlines()]
n_row = len(raw_input)
n_column = len(raw_input[0])

def print_map(map):
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    for line in map:
        print("".join(line))
    # sleep()


def step(map):
    map_old = [[c for c in line] for line in map]
    counter = 0
    # move right
    for i_y, line in enumerate(map_old):
        for i_x, c in enumerate(line):
            i_x_2 = i_x + 1
            if i_x_2 == n_column:
                i_x_2 = 0
            c_2 = map_old[i_y][i_x_2]
            if c == ">" and c_2 == ".":
                map[i_y][i_x] = "."
                map[i_y][i_x_2] = ">"
                counter += 1
    print_map(map)
    # move down
    map_old = [[c for c in line] for line in map]
    for i_y, line in enumerate(map_old):
        for i_x, c in enumerate(line):
            i_y_2 = i_y + 1
            if i_y_2 == n_row:
                i_y_2 = 0
            c_2 = map_old[i_y_2][i_x]
            if c == "v" and c_2 == "." and map[i_y_2][i_x] == ".":
                map[i_y][i_x] = "."
                map[i_y_2][i_x] = "v"
                counter += 1

    print_map(map)
    if counter == 0:
        return None
    return map

for i in range(10000):
    raw_input = step(raw_input)
    if raw_input is None:
        print(i + 1)
        break