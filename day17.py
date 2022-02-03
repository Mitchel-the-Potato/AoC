min_x, max_x, min_y, max_y = 124, 174, -123, -86

def check_valid_vx(vx, min_x, max_x):
    output = []
    distance = 0
    for step in range(1, 10000):
        distance += vx
        vx = vx-1 if vx>0 else 0
        if distance >= min_x and distance <= max_x:
            output.append(step)
        if distance > max_x:
            break
    return output

total_list = []
for vx in range(11, 100):
    # print(vx, check_valid_vx(vx, min_x, max_x))
    t = check_valid_vx(vx, min_x, max_x)
    print("start vx = {}, steps to arrive in target: {}".format(vx, t))
    total_list.extend(t)

max_step = 10000

def check_valid_vy(vy, max_step=max_step, min_y=min_y, max_y=max_y):
    highest = 0
    distance = 0
    for step in range(1, max_step + 1):
        distance += vy
        vy -= 1

        highest = max(highest, distance)
        # print(step, distance)
        if distance >= min_y and distance <= max_y:
            return highest#, step, distance
        if distance < min_y:
            break
    return 0

# check_valid_vy(4)

# print(max([check_valid_vy(vy) for vy in range(1, 10000)]))


#2


print(total_list)


def check_valid_vy_V2(vy, steps, min_y=min_y, max_y=max_y):
    distance = 0
    if len(steps) == 0:
        return 0
    for step in range(1, max(steps)+1):
        distance += vy
        vy -= 1
        if step in steps:
            if (distance >= min_y) and (distance <= max_y):
                return 1

        if distance < min_y:
            break

    return 0


answer = 0
for x in range(0, 175):
    steps = check_valid_vx(x, min_x, max_x)
    print(x, steps, answer)
    for y in range(-130, 10000):
        answer += check_valid_vy_V2(y, steps, min_y, max_y)


print(answer)
