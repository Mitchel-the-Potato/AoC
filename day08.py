
from collections import Counter

with open("day08_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

wrong_displays = [a.split("|") for a in raw_input]

def find_len_list(segments, n):
    filted = [l for l in segments if len(l) == n]
    assert len(filted) == 1
    return filted[0]

def get_147(smess):
    segments = smess.split()

    found = []
    for n in [2, 4, 3]:
        this_str = find_len_list(segments, n)
        found.append(this_str)
    return found


def training(smess):
    letter_occurance = Counter(smess.replace(" ", ""))

    str_1, str_4, str_7 = get_147(smess)
    assert len(letter_occurance) == 7
    mapping = dict()
    for wrong_letter, number_of_wrong_letter in letter_occurance.items():
        if number_of_wrong_letter == 6:
            mapping[wrong_letter] = "b"
        elif number_of_wrong_letter == 4:
            mapping[wrong_letter] = "e"
        elif number_of_wrong_letter == 9:
            mapping[wrong_letter] = "f"
        elif number_of_wrong_letter == 7:
            if wrong_letter in str_4:
                mapping[wrong_letter] = "d"
            else:
                mapping[wrong_letter] = "g"
        elif number_of_wrong_letter == 8:
            if wrong_letter in str_1:
                mapping[wrong_letter] = "c"
            else:
                mapping[wrong_letter] = "a"
    mapping[" "] = " "
    return mapping

def convert(mapping, s_test):
    str_wrong_to_correct = [mapping[a] for a in s_test]
    str_join = "".join(str_wrong_to_correct)
    str_split = str_join.split()
    str_segments = ["".join(sorted(a)) for a in str_split]


    map_segment_to_number = dict()
    map_segment_to_number["abcefg"] = 0
    map_segment_to_number["cf"] = 1
    map_segment_to_number["acdeg"] = 2
    map_segment_to_number["acdfg"] = 3
    map_segment_to_number["bcdf"] = 4
    map_segment_to_number["abdfg"] = 5
    map_segment_to_number["abdefg"] = 6
    map_segment_to_number["acf"] = 7
    map_segment_to_number["abcdefg"] = 8
    map_segment_to_number["abcdfg"] = 9

    number_correct = [map_segment_to_number[s] for s in str_segments]
    return number_correct

all_numbers = []
all_4_numbers = []
for s_train, s_test in wrong_displays:
    # print("{} -> {}".format(s_train, s_test))
    mapping = training(s_train)
    numbers = convert(mapping, s_test.strip())
    #print(numbers)
    all_numbers.extend(numbers)
    all_4_numbers.append(int("".join([str(b) for b in numbers])))
print(all_numbers)

counts = Counter(all_numbers)

print(counts[1] + counts[4] + counts[7] + counts[8])

print(all_4_numbers)
print(sum(all_4_numbers))