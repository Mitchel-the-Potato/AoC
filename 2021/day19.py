import re
from collections import Counter
from pprint import pprint


def parse_input(fn_input):
    scans = {}

    pattern = re.compile("--- scanner (\d+) ---")

    with open("day19_input.txt", "r") as f:
        for line in f.readlines():
            if line.startswith("---"):
                # start a new scanner
                i = int(pattern.findall(line)[0])
                assert i not in scans
                scans[i] = []
            elif len(line.strip()) == 0:
                continue
            else:
                pos = [int(a) for a in line.strip().split(",")]
                scans[i].append(pos)
    return scans


def rotate_point_90(p, dim, n=1):
    if n == 0:
        return p

    if dim == 0:
        p2 = (p[0], -p[2], p[1])
    elif dim == 1:
        p2 = (-p[2], p[1], p[0])
    elif dim == 2:
        p2 = (-p[1], p[0], p[2])
    else:
        raise NotImplementedError

    if n == 1:
        return p2
    else:
        assert n > 1
        return rotate_point_90(p2, dim, n - 1)


def rotate_beacons(beacon_list, dim, n):
    return [rotate_point_90(p, dim, n) for p in beacon_list]


# test rotation
a = [1, 2, 3]
for n in range(5):
    print(rotate_point_90(a, 1, n))
# note: the last one must be same as first one

[1, 2, 3]
(-3, 2, 1)
(-1, 2, -3)
(3, 2, -1)
(1, 2, 3)


def rotate_all(bl):
    rotated = []
    for nx in range(4):
        t1 = rotate_beacons(bl, 0, nx)
        for ny in range(4):
            t2 = rotate_beacons(t1, 1, ny)
            for nz in range(4):
                t3 = rotate_beacons(t2, 2, nz)
                rotated.append((t3, (nx, ny, nz)))
    return rotated


def match_x(bl1, bl2):
    distances = [a[0] - b[0] for a in bl1 for b in bl2]
    counts = Counter(distances)
    possible = []
    for distance, count in counts.most_common():
        if count < 12:
            break
        pairs = [(i1, i2) for i1, a in enumerate(bl1) for i2, b in enumerate(bl2) if (a[0] - b[0]) == distance]
        possible.append((pairs, distance))
    # print("x found {}".format(len(possible)))
    return possible


def filter_yz(possible, bl1, bl2):
    checked = []
    for pairs, offset_x in possible:
        offsets = [offset_x]
        for dim in [1, 2]:
            distance = [bl1[i1][dim] - bl2[i2][dim] for (i1, i2) in pairs]
            d, n = Counter(distance).most_common(1)[0]
            if n < 12:
                break  # fail
            offsets.append(d)
        else:
            # now success
            checked.append((tuple(pairs), tuple(offsets)))
    return checked


def match_beacons(bl1, bl2):
    return filter_yz(match_x(bl1, bl2), bl1, bl2)


def get_chains(ks, n_key=32):
    chains = {0: None}
    for i in range(n_key):
        for k1, k2 in ks:
            # print(k1, k2)
            if k2 not in chains:
                if k1 == 0:
                    chains[k2] = [k1, k2]
                else:
                    if k1 in chains:
                        chains[k2] = chains[k1] + [k2]

    return chains


def transfer_scanner(bl, rotates, offsets):
    t1 = bl
    for i_dim in range(3):
        t1 = rotate_beacons(t1, i_dim, rotates[i_dim])
    t1 = [(x + offsets[0], y + offsets[1], z + offsets[2]) for x, y, z in t1]
    return t1


def transfer_scanner_final(bl, convert_chain, between_scanners):
    t = bl
    for i_step in list(range(len(convert_chain) - 1, 0, -1)):
        s_from = convert_chain[i_step - 1]
        s_to = convert_chain[i_step]
        rotates, offsets = between_scanners[(s_from, s_to)]
        t = transfer_scanner(t, rotates, offsets)
    return t


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

scans = parse_input("day19_input.txt")
# print(scans)

scanner_index = list(range(len(scans)))
for k, v in scans.items():
    print("{}: {}".format(k, len(v)))

    between_scanners = {}
    for k1, v1 in scans.items():
        for k2, v2 in scans.items():
            if k1 == k2:
                continue

            possible_all = []
            for i_rota, (bl2, rotates) in enumerate(rotate_all(v2)):
                # print("new rotate:", k1, k2, i_rota, rotates, bl2)
                possible = match_beacons(v1, bl2)
                assert len(possible) <= 1
                if len(possible) == 0:
                    continue
                # print(possible)
                pairs, offsets = possible[0]
                possible_all.append((rotates, offsets))
                # print("matched: {} vs {}, rotation:{}".format(k1, k2, rotates))

            if len(possible_all) > 0:
                # some diff by rotations. just pick 1st one.
                between_scanners[(k1, k2)] = possible_all[0]

    pprint(between_scanners)

chains = get_chains(between_scanners.keys())
pprint(chains)
assert len(chains) == len(scans)

for i in range(1,32):
    t = transfer_scanner_final(scans[i], chains[i], between_scanners)
    print(i, match_beacons(scans[0], t))


#Q1
beacons = set([tuple((b for b in a)) for a in scans[0]])
# print(beacons)
for i in range(1, 32):
    t = transfer_scanner_final(scans[i], chains[i], between_scanners)
    # print(i, t)
    for t1 in t:
        beacons.add(t1)
    # print(i, len(beacons))

print(len(beacons))

#Q2

scanners = [(0, 0, 0)]
for i in range(1, 32):
    t = transfer_scanner_final([(0,0,0)], chains[i], between_scanners)
    scanners.append(t[0])

pprint(scanners)

distances = [manhattan_distance(s1, s2) for s1 in scanners for s2 in scanners]
# print(distances)
print(max(distances))
