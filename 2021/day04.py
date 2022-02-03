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

def last_bingo(blocks):
    left_blocks = list(range(100))
    for num in numbersequence:
        for i_left in left_blocks:
            blocks[i_left] = markblock(blocks[i_left], num)
            if check_bingo(blocks[i_left]):
                if len(left_blocks) == 1:
                    return num, blocks[i_left]
                else:
                    left_blocks.remove(i_left)
                    print(num, len(left_blocks))

def last_bingo_v2(blocks):
    for num in numbersequence:
        blocks = [markblock(block, num) for block in blocks]
        left_blocks = [block for block in blocks if not check_bingo(block)]
        if len(left_blocks) == 0:
            assert len(blocks) == 1
            return num, blocks[0]
        blocks = left_blocks





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

number, block = last_bingo_v2(blocks)
print(number, block)
sum = sum_of_block(block)
print(sum*number)