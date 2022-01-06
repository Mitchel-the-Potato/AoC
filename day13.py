with open("day13_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

def parse_position(s_position):
    x, y = s_position.split(",")
    return int(y), int(x)

def print_paper(paper):
    for line in paper:
        print("".join(line))

def new_paper(n_row, n_col):
    return [["." for x in range(n_col)] for y in range(n_row)]

dot_positions = [parse_position(line) for line in raw_input]
n_row = max([a[0] for a in dot_positions]) + 1
n_col = max([a[1] for a in dot_positions]) + 1

paper = new_paper(n_row, n_col)
for y, x in dot_positions:
    paper[y][x] = "#"
print_paper(paper)

print("y:{},x:{}".format(n_row, n_col))

def fold_paper(paper, x_or_y, line_number):
    n_y = len(paper)
    n_x = len(paper[0])
    if x_or_y == "x":
        assert line_number == int((n_x-1)/2)
        paper2 = new_paper(n_y, line_number)
        for y in range(n_y):
            for x in range(line_number):
                point_1 = paper[y][x]
                point_2 = paper[y][line_number * 2 - x]
                if point_1 == "#" or point_2 == "#":
                    new_value = "#"
                else:
                    new_value = "."
                paper2[y][x] = new_value
    else:
        assert line_number == int((n_y-1)/2)
        paper2 = new_paper(line_number, n_x)
        for y in range(line_number):
            for x in range(n_x):
                point_1 = paper[y][x]
                point_2 = paper[line_number * 2 - y][x]
                if point_1 == "#" or point_2 == "#":
                    new_value = "#"
                else:
                    new_value = " "
                paper2[y][x] = new_value

    return paper2

with open("day13_2_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]


def parse_fold(line):
    a, b = line.replace("fold along ", "").split("=")
    return a, int(b)

def count_dots(paper):
    n_dot = 0
    for line in paper:
        for c in line:
            if c == "#":
                n_dot += 1
    return n_dot

fold_rules = [parse_fold(line) for line in raw_input]

for rule in fold_rules:
    paper = fold_paper(paper, rule[0], rule[1])
    print(count_dots(paper))

print_paper(paper)


