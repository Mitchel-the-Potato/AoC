#! /usr/bin/env python3

from itertools import chain
from heapq import heappush, heappop

inf = float("inf")

with open("day15_input.txt", "r") as f:
    matrix = [[int(a) for a in line.strip()] for line in f.readlines()]

def print_matrix(matrix, join=""):
    for i_row in range(len(matrix)):
        print(join.join([str(a) for a in matrix[i_row]]))

def clip(num):
    if num <= 9:
        return num
    else:
        return num - 9


def expand_matrix_x(matrix):
    def expand_line_x(line):
        lines = [[clip(a+i) for a in line] for i in range(5)]
        return list(chain(*lines))
    return [expand_line_x(line) for line in matrix]

def expand_matrix_y(matrix):
    def copy_matrix_offset(matrix, offset):
        return [[clip(a+offset) for a in line] for line in matrix]
    temp = [copy_matrix_offset(matrix, a) for a in range(5)]
    return list(chain(*temp))

m5x5 = expand_matrix_y(expand_matrix_x(matrix))

# NOTE: uncomment below for Q2
matrix = m5x5
N_COL = len(matrix[0])
N_ROW = len(matrix)

matrix[0][0] = 0

def heuristic(point, target=(N_ROW-1, N_COL-1)):
    # just use the distance of the point to target as heuristic estimation
    # also works if return 0
    y, x = point
    ty, tx = target
    return (ty + tx - y - x) * 1

def get_neighbours(point):
    global matrix, N_COL, N_ROW
    # get neighbours (of point) and their values
    neigher_offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    y, x = point
    neighbour = [(y+dy, x+dx) for dy, dx in neigher_offsets]
    def is_valid(p):
        return p[0] >= 0 and p[0] < N_ROW and p[1] >= 0 and p[1] < N_COL
    def get_value(p):
        return matrix[p[0]][p[1]]
    return {p:get_value(p) for p in neighbour if is_valid(p)}

def a_star(get_neighbours, p_start=(0, 0), p_target=(N_ROW-1, N_COL-1), h=heuristic):
    global matrix
    # snippet from `Python Algorithms` p204. By Magnus Lie Hetland
    visited, Q = {}, [(h(p_start), None, p_start)]
    while Q:
        d, p_prev, p_curr = heappop(Q)
        # NOTE: heappop will automatically yield current point with SMALLEST estimated loss
        # always start from this smallest point
        if p_curr in visited:
            continue
        visited[p_curr] = p_prev
        if p_curr == p_target:
            return d - h(p_target), visited
        for p_neighbor, neighbour_loss in get_neighbours(p_curr).items():
            # estimate delta weight to add.
            # neighbour_loss is given by task. then add neighbour's distance.
            delta_w = neighbour_loss - h(p_curr) + h(p_neighbor)
            heappush(Q, (d + delta_w, p_curr, p_neighbor))
    return inf, None

loss, visited = a_star(get_neighbours)
# visited is a dictionary, we can use it to find the whole path.
print(loss)