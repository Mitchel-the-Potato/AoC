with open("day06_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]


lanternfish_internal_timers = [int(a) for a in raw_input[0].split(",")]
print(lanternfish_internal_timers)

def next_day(timer):
    if timer == 0:
        return 6
    else:
        return timer - 1

def create_new_fish(timers):
    new_fish = [8 for timer in timers if timer == 0]
    return new_fish

for day in range(0, 80):
    new_fish = create_new_fish(lanternfish_internal_timers)
    lanternfish_internal_timers = [next_day(timer) for timer in lanternfish_internal_timers]
    lanternfish_internal_timers  = lanternfish_internal_timers + new_fish

print(len(lanternfish_internal_timers))


