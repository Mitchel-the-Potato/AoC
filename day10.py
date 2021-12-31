with open("day10_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

lines = [[a for a in line.strip()] for line in raw_input]

scores = dict()
scores["}"] = 1197
scores[")"] = 3
scores[">"] = 25137
scores["]"] = 57

mapping_pairs = dict()
mapping_pairs["}"] = "{"
mapping_pairs[")"] = "("
mapping_pairs[">"] = "<"
mapping_pairs["]"] = "["

def check_line(line):
    stack = []
    for c in line:
        if c in mapping_pairs.keys():
            # print(c, stack)
            c_pop = stack.pop()
            c_correct = mapping_pairs[c]
            if c_pop != c_correct:
                return scores[c]
        else:
            stack.append(c)
    return 0

total_scores = [check_line(line) for line in lines]
print(total_scores)
print(sum(total_scores))

# q2
scores_v2 = dict()
scores_v2["{"] = 3
scores_v2["("] = 1
scores_v2["<"] = 4
scores_v2["["] = 2

def translate_into_number(score_list, step=5):
    if len(score_list) == 1:
        return score_list[0]
    else:
        last_one = score_list.pop()
        return last_one + translate_into_number(score_list)*step

def check_line_v2(line):
    stack = []
    for c in line:
        if c in mapping_pairs.keys():
            c_pop = stack.pop()
            c_correct = mapping_pairs[c]
            assert c_pop == c_correct
        else:
            stack.append(c)
    score = [scores_v2[a] for a in stack]
    score_revers = score[::-1]
    print("".join(stack), score, score_revers)
    return translate_into_number(score_revers)

lines_incomplete = [line for i, line in enumerate(lines) if total_scores[i] == 0]
print("total lines read: {}, incomplete lines: {}".format((len(lines)), len(lines_incomplete)))
scores_q2 = [check_line_v2(line) for line in lines_incomplete]
print(scores_q2)
sortedSORTEDSLDFJ = sorted(scores_q2)
n_mid = int((len(sortedSORTEDSLDFJ)+1) / 2)
print(sortedSORTEDSLDFJ)
print(sortedSORTEDSLDFJ[n_mid-1])
