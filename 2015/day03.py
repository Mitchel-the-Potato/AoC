from collections import Counter


with open("2015_day03_input.txt", "r") as f:
    instructions = [a for a in f.readline()]

print(instructions)

def move(instructions):
    santa_current_position = (0, 0)
    robot_current_position = (0, 0)
    each_location = [(0, 0)]

    for i, a in enumerate(instructions):
        is_even = i % 2
        if is_even:
            if a == ">":
                santa_current_position = (santa_current_position[0] + 1, santa_current_position[1])
            elif a == "<":
                santa_current_position = (santa_current_position[0] - 1, santa_current_position[1])
            elif a == "^":
                santa_current_position = (santa_current_position[0], santa_current_position[1] + 1)
            elif a == "v":
                santa_current_position = (santa_current_position[0], santa_current_position[1] - 1)
            each_location.append(santa_current_position)
        else:
            if a == ">":
                robot_current_position = (robot_current_position[0] + 1, robot_current_position[1])
            elif a == "<":
                robot_current_position = (robot_current_position[0] - 1, robot_current_position[1])
            elif a == "^":
                robot_current_position = (robot_current_position[0], robot_current_position[1] + 1)
            elif a == "v":
                robot_current_position = (robot_current_position[0], robot_current_position[1] - 1)
            each_location.append(robot_current_position)

    count = Counter(each_location)
    print(count)
    return count

total_count = move(instructions)

answer = 0

for location, n in total_count.items():
    if n >= 1:
        answer += 1

print(answer)
