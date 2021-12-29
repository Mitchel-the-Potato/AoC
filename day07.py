import sys
sys.setrecursionlimit(3000)
from functools import lru_cache

with open("day07_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

crab_arrangement_height = [int(a) for a in raw_input[0].split(",")]

max_height = max(crab_arrangement_height)
min_height = min(crab_arrangement_height)

fuel_used_for_original_height = dict()

steps_to_fuel = dict()
steps_to_fuel[0] = 0
for height in range(1, max_height + 1):
    steps_to_fuel[height] = steps_to_fuel[height - 1] + height

@lru_cache(3000)
def step2fuel(step):  #Epic move right here
    if step == 0:
        return 0
    else:
        return step + step2fuel(step - 1)

def calculate_fuel(current_height, target_height):
    return abs(current_height - target_height)

def calculate_fuel_v2(current_height, target_height):
    return steps_to_fuel[abs(current_height - target_height)]

def calculate_fuel_v3(current_height, target_height):
    return step2fuel(abs(current_height - target_height))

for height in range(min_height, max_height + 1):
    all_fuels = [calculate_fuel_v3(a, height) for a in crab_arrangement_height]
    fuel_used_for_original_height[height] = sum(all_fuels)

print(min(fuel_used_for_original_height.values()))

