from collections import defaultdict
from copy import  copy

#########################################
# parse input
with open("day12_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

raw_input_2 = [line.strip().split("-") for line in raw_input]
print(raw_input_2)

paths = defaultdict(list)
print("graph {")
for a, b in raw_input_2:
    print("    {} -- {};".format(a, b))

print("}")
print("dot -Tpng plot.dot -o plot.png")