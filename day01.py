#! /usr/bin/env python3

with open("day01_input.txt", "r") as f:
    depths = [int(a) for a in f.readlines()]

larger_counts = [(a, b) for (a, b) in zip(depths[0:1999], depths[1:2000]) if b>a]

print(larger_counts)
print(len(larger_counts))

sumed = [a+b+c for (a, b, c) in zip(depths[0:1998], depths[1:1999], depths[2:2000]) ]

larger_counts = [(a, b) for (a, b) in zip(sumed[0:len(sumed)-1], sumed[1:len(sumed)]) if b>a]
print(len(larger_counts))


# larger_count = 0
# for i in range(1, 2000):
#     prev = depths[i-1]
#     curr = depths[i]
#     if curr > prev:
#         larger_count = larger_count + 1
#         # larger_count += 1
# print(larger_count)