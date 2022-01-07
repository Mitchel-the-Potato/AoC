import sys
sys.setrecursionlimit(3000)
from functools import lru_cache

from collections import Counter

with open("day14_2_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]
inputs = raw_input[0]


def convert_rules_line(rule):
    k, v = rule.strip().split(" -> ")
    v2 = v + k[1]
    return k, v2

with open("day14_input.txt", "r") as f:
    raw_rules = [convert_rules_line(a) for a in f.readlines()]



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

#Q2
def string_to_pairs(ringst):
    pairs = []
    for i, c in enumerate(ringst):
        if i == 0:
            continue
        else:
            pairs.append(ringst[i-1 : i+1])
    return pairs

@lru_cache(100)
def expand_pair(pair):

    for i in range(10):
        output = [pair[0]]
        for keys in string_to_pairs(pair):
            output.append(rules[keys])
        pair = "".join(output)
    return pair


print("BN -> {}".format(expand_pair("BN")))


@lru_cache(500)
def repeat_pair(pair, n):
    assert n in [10, 20, 30, 40, 50, 60]
    if n == 10:
        expand_string = expand_pair(pair)
        count = Counter(expand_string[1:])
        return count
    else:
        expand_string = expand_pair(pair)
        count = Counter()
        for pear in string_to_pairs(expand_string):
            this_count = repeat_pair(pear, n-10)
            count = count + this_count
        return count


def repeat_string(s, n):
    count = Counter()
    pairs = string_to_pairs(s)
    for pair in pairs:
        this_count = repeat_pair(pair, n)
        count = count + this_count
    count[s[0]] += 1
    return count

print(repeat_string(inputs, 40))