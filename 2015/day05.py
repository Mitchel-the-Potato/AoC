
with open("2015_day05_input.txt", "r") as f:
    lines = [a.strip() for a in f.readlines()]
for line in lines:
    print(line)

def check_line(line):
    a = "ab"
    b = "cd"
    c = "pq"
    d = "xy"
    counter_for_vowel = 0
    true_counter = 0
    if a in line or b in line or c in line or d in line:
        return False


    for x in line:
        if x in ("a", "e", "i", "o", "u"):
            counter_for_vowel += 1
    if counter_for_vowel < 3:
        return False


    for i in range(len(line) -1):
        c = line[i]
        d = line[i+1]
        if c == d:
            break
    else:
        return False
    mini_counter = 0
    for i in range(len(line) -1):
        a = line[i]
        b = line[i+1]
        if (a, b) == ("a", "b") or (a, b) == ("c", "d") or (a, b) == ("p", "q") or (a, b) == ("x", "y"):
            return False

    return True


nice_strings = 0
bad_strings = 0
for line in lines:
    if check_line(line) == True:
        nice_strings += 1
    else:
        bad_strings += 1

print(nice_strings)


#Q2

def check_linev2(line):
    found_cond1 = False
    for i in range(len(line) - 1):
        c = line[i]
        d = line[i + 1]
        line2 = line[i+2:]
        for j in range(len(line2) - 1):
            a = line2[j]
            b = line2[j+1]
            if c == a and d == b:
                found_cond1 = True
                break
        if found_cond1:
            break
    else:
        return False

    for i in range(len(line) - 2):
        c = line[i]
        d = line[i + 2]
        if c == d:
            break
    else:
        return False

    return True

print(check_linev2("abadfjslkdjlfljdf"))

nice_strings = 0
bad_strings = 0
for line in lines:
    if check_linev2(line) == True:
        nice_strings += 1
    else:
        bad_strings += 1

print(nice_strings)



