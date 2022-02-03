with open("day02_input.txt", "r") as f:
    depths = [a for a in f.readlines()]
x = 0
y = 0
aim = 0
for command in depths:
    c, number = command.split(" ")
    if c == "forward":
        x += int(number)
        y += aim*int(number)
    elif c == "down":
        aim += int(number)
    elif c == "up":
        aim -= int(number)
    else:
        print(c)

print(x, y, x*y)