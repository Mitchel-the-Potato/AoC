from collections import defaultdict
from copy import  copy

#########################################
# parse input
with open("day12_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

raw_input_2 = [line.strip().split("-") for line in raw_input]
print(raw_input_2)

paths = defaultdict(list)
for a, b in raw_input_2:
    paths[a].append(b)
    paths[b].append(a)

#########################################
def is_small_cave(point):
    return point == point.lower()


good_path = 0
def walk_to_point(n_occurance, point, twice_used):
    global good_path
    if is_small_cave(point) and n_occurance[point] >= 1:
        if twice_used:
            return
        else:
            twice_used = True
    if point == "start" and n_occurance[point] >= 1:
        return
    n_occu = copy(n_occurance)
    n_occu[point] += 1

    if point == "end":
        good_path += 1
        if good_path % 10000 == 0:
            print(n_occu)
        return

    for p in paths[point]:
        walk_to_point(n_occu, p, twice_used)

walk_to_point(defaultdict(int), "start", twice_used=False)
# print(good_path)
# print(paths)
print((good_path))
