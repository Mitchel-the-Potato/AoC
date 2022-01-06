from collections import Counter

with open("day14_2_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]


def convert_rules_line(rule):
    k, v = rule.strip().split(" -> ")
    v2 = v + k[1]
    return k, v2

with open("day14_input.txt", "r") as f:
    raw_rules = [convert_rules_line(a) for a in f.readlines()]

inputs = raw_input[0]


rules = {k:v for k, v in raw_rules}
print(raw_rules)
print(rules)


def insert_character(s):
    output = ""
    for i, character in enumerate(inputs):
        if i == 0:
            output += character
        else:
            k = inputs[i - 1: i + 1]
            v = rules.get(k, character)
            output += v
    return output

for i in range(40):
    inputs = insert_character("CN")

print(inputs)
print(len(inputs))

count = Counter(inputs)
print(count)