with open("day05_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

def translate(s):
    a, b = s.split("->")
    c1, c2 = a.split(",")
    c3, c4 = b.split(",")
    return int(c1), int(c2), int(c3), int(c4)

print(translate(raw_input[0]))

lines = [translate(s) for s in raw_input]
print(lines)

plot = [[0 for i_x in range(1000)] for i_y in range(1000)]

# draw line
for c1, c2, c3, c4 in lines:
    # assert c1 == c3 or c2 == c4, "numbers not match: {}, {}, {}, {}".format(c1, c2, c3, c4)


    if c1 == c3 or c2 == c4:
        if c1 > c3:
            c1, c3 = c3, c1
        if c2 > c4:
            c2, c4 = c4, c2
        for i_y in range(c1, c3+1):
            for i_x in range(c2, c4+1):
                plot[i_y][i_x] += 1
    else:
        if c1 > c3:
            step_y = -1
        else:
            step_y = 1
        if c2 > c4:
            step_x = -1
        else:
            step_x = 1
        line_location = zip(list(range(c1, c3+step_y, step_y)), list(range(c2, c4+step_x, step_x)))
        for i_y, i_x in line_location:
            plot[i_y][i_x] += 1


#count overlap
final_count = 0
for line in plot:
    for number in line:
        if number > 1:
            final_count += 1

print(final_count)
