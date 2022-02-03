

# prepare input
with open("day20_input.txt", "r") as f:
    image_origin = [[a for a in line.strip()] for line in f.readlines()]

def expand_image(image):
    # NOTE: only expand once.

    # TRICKY!
    # examine the first / last char of day20_algirithm.txt,
    # need to understand what they corresponding

    # each enhancement will increase boundary by 1 (ignore the very outside)
    # the offset must be large enough to contain for ALL enhancements.
    offset = 60

    m_y = len(image) + offset*2
    m_x = len(image[0]) + offset*2
    image_2 = [[None for x in range(m_x)] for y in range(m_y)]

    for j_y in range(m_y):
        i_y = j_y - offset # in old image
        for j_x in range(m_x):
            i_x = j_x - offset # in old image
            if i_y < 0 or i_x < 0 or i_y>= len(image) or i_x >= len(image[0]):
                image_2[j_y][j_x] = "."
            else:
                image_2[j_y][j_x] = image[i_y][i_x]

    return image_2

image = expand_image(image_origin)

with open("day20_1_input.txt", "r") as f:
    algoirithm = [a for a in f.readline().strip()]
    assert len(algoirithm) == 512


def plot_image(image):
    for line in image:
        print("".join(line))
    print("\n\n")

def count_pixel_lit(image):
    return sum([sum([1 if a=="#" else 0 for a in line]) for line in image])

plot_image(image)
print(count_pixel_lit(image))
print("".join(algoirithm))

# functions
def pick_nine_pixels(image, i_y, i_x):
    n_y = len(image)
    n_x = len(image[0])

    convert = {".":"0", "#":"1"}

    pixels = []
    for j_y in [i_y-1, i_y, i_y+1]:
        for j_x in [i_x-1, i_x, i_x+1]:
            if j_y < 0 or j_y >= n_y or j_x < 0 or j_x >= n_x:
                pixels.append("0") # default is . -> 0
            else:
                pixels.append(convert[image[j_y][j_x]])

    s_bin = "".join(pixels)
    return s_bin

def pixel2pixel(image, i_y, i_x):
    s_bin = pick_nine_pixels(image, i_y, i_x)
    index = int(s_bin, base=2)
    # if index == 511:
    #     print("{},{} -> {} -> {} -> {}".format(i_y, i_x, s_bin, index, algoirithm[index]))
    return algoirithm[index]

def image2image(image, outside="."):
    n_y = len(image)
    n_x = len(image[0])
    # trick here: the outside edge is flipping every time.
    image_2 = [[outside for x in range(n_x)] for y in range(n_y)]

    # don't touch the edge
    for j_y in range(1, n_y-1):
        for j_x in range(1, n_x-1):
            image_2[j_y][j_x] = pixel2pixel(image, j_y, j_x)

    return image_2


# Q1
n = 2
# Q2
n = 50

outsides = {0: ".", 1:"#"}
for i in range(n):
    image = image2image(image, outsides[(i+1)%2])
    # plot_image(image)
    print(count_pixel_lit(image))