import sys
sys.setrecursionlimit(3000)

from itertools import chain
from collections import Counter

with open("day09_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

height_map = [[int(a) for a in line.strip()] for line in raw_input]
print(height_map)

n_column = len(height_map[0])
n_row = len(height_map)

def is_valid(neighbor):
    y = neighbor[0]
    x = neighbor[1]
    if y < 0 or x < 0:
        return False
    if y >= n_row or x >= n_column:
        return False
    return True

def get_height(neighbor):
    y, x = neighbor
    return height_map[y][x]


smallest_heights = 0
for i_row in range(n_row):
    for i_column in range(n_column):
        current_location = (i_row, i_column)
        current_hight = get_height(current_location)
        neighbors = [(i_row + 1, i_column), (i_row - 1, i_column), (i_row, i_column + 1), (i_row, i_column - 1)]
        neighbors_valid = [neighbor for neighbor in neighbors if is_valid(neighbor)]
        neighbors_compared = [current_hight < get_height(neighbor) for neighbor in neighbors_valid]
        # print(neighbors_compared)
        is_smallest = all(neighbors_compared)
        if is_smallest:
            smallest_heights += current_hight + 1

print(smallest_heights)

# q2
def is_edge(height):
    if height == 9 or type(height) is str:
        return True
    else:
        return False

def mark_basin(location, basin_number):
    # print(location, basin_number)
    if not is_valid(location):
        return
    y, x = location
    if is_edge(height_map[y][x]):
        return
    height_map[y][x] = basin_number

    neighbors = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    for neighbor in neighbors:
        y, x = neighbor
        if not is_valid(neighbor):
            continue
        neighbor_height = height_map[y][x]
        if not is_edge(neighbor_height):
            # print(neighbor, neighbor_height, basin_number)
            mark_basin(neighbor, basin_number)


basin_index = 0
for i_row in range(n_row):
    for i_column in range(n_column):
        current_height = height_map[i_row][i_column]
        if not is_edge(current_height):
            basin_index += 1
            basin_number = "b{:03d}".format(basin_index)
            mark_basin((i_row, i_column), basin_number)

# print(height_map)
flatten_map = list(chain(*height_map))
# print(flatten_map)
count = Counter(flatten_map)
del count[9]
count_2 = sorted(count.values(), reverse=True)
print(count_2[0] * count_2[1] * count_2[2])

