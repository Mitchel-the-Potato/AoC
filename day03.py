with open("day03_input.txt", "r") as f:
    depths = [a for a in f.readlines()]

n_lines = len(depths)
counter = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in depths:
    for i,character in enumerate(line):
        if character == "1":
            counter[i] += 1

gamma = "0b"
epsilon = "0b"
for number in counter:
    if number > n_lines/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(counter)


i_gamma = int(gamma, 2)
i_epsilon = int(epsilon, 2)
print(i_gamma*i_epsilon)


######################
# life support
def count_in_column(lines, i):
    n_0 = 0
    n_1 = 0
    for line in lines:
        if line[i] == "1":
            n_1 += 1
        else:
            n_0 += 1
    if n_1 >= n_0:
        return "1"
    else:
        return "0"

def find_most_common(depths):
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        check_char = count_in_column(depths, i)
        left_lines = [line for line in depths if line[i] == check_char]
        if len(left_lines) == 1:
            return left_lines[0]
        depths = left_lines


def least_common_char(lines, i):
    n_0 = 0
    n_1 = 0
    for line in lines:
        if line[i] == "1":
            n_1 += 1
        else:
            n_0 += 1
    if n_1 >= n_0:
        return "0"
    else:
        return "1"

def least_common_lines(depths):
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        check_char = least_common_char(depths, i)
        left_lines = [line for line in depths if line[i] == check_char]
        if len(left_lines) == 1:
            return left_lines[0]
        depths = left_lines

Co2 = least_common_lines(depths)
oxygen = find_most_common(depths)

oxygeni = int(oxygen, 2)
Co2i = int(Co2, 2)
print(oxygeni*Co2i)