from pprint import pprint

with open("day04_input.txt", "r") as f:
    depths = [a for a in f.readlines()]

numbersequence = depths[0].split(",")
numbersequence = [int(a) for a in numbersequence]
print(numbersequence)
blocks = []
block = []
for i in range(1, len(depths)):
    if depths[i] == "\n":
        assert len(block) == 0 or len(block) == 5
        block = []
    else:
        ss = depths[i].split()
        ii = [int(a) for a in ss]
        assert len(ii) == 5
        block.append(ii)
        if len(block) == 5:
            blocks.append(block)


# pprint(blocks)
print(len(blocks))

pprint(blocks[0])
pprint(blocks[0][0])
pprint(blocks[0][0][0])


def markblock(block, number):
    for i_row in range(5):
        for i_col in range(5):
            if block[i_row][i_col] == number:
                block[i_row][i_col] = -1
    return block

def check_bingo(block):
    for i_row in range(5):
        this_row = block[i_row]
        if all([a == -1 for a in this_row]):
            return True
    for i_col in range(5):
        this_col = [line[i_col] for line in block]
        if all([b == -1 for b in this_col]):
            return True
    return False

def last_bingo():
    left_blocks = list(range(100))
    for number in numbersequence:
        for i in left_blocks:
            blocks[i] = markblock(blocks[i], number)
            if check_bingo(blocks[i]):
                if len(left_blocks) == 1:
                    return number, blocks[i]
                else:
                    left_blocks.remove(i)
                    print(number, len(left_blocks))

def play_bingo():
    for number in numbersequence:
        for i in range(100):
            print(i)
            blocks[i] = markblock(blocks[i], number)
            pprint(blocks[i])
            if check_bingo(blocks[i]):
                return number, blocks[i]



def sum_of_block(block):
    sum = 0
    for i_row in range(5):
        for i_col in range(5):
            if block[i_col][i_row] >= 0:
                sum += block[i_col][i_row]
    return sum

number, block = last_bingo()
print(number, block)
sum = sum_of_block(block)
print(sum*number)