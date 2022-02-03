#! /usr/bin/env python3

import math

with open("day16_input.txt", "r") as f:
    s_hex = f.readlines()[0].strip()

def hex2bin(s_hex):
    ss = [bin(int(a, 16))[2:].zfill(4) for a in s_hex]
    return "".join(ss)

def parse_literal_num(l_bin):
    print("parse literal number: {}".format("".join(l_bin)))
    nums = ""
    while True:
        a = l_bin[0]
        b = l_bin[1:5]
        nums += b
        l_bin = l_bin[5:]
        if a == "0":
            break
    return int(nums, 2), l_bin

all_version = []

id2fun = {
        0: sum,
        1: math.prod,
        2: min,
        3: max,
        5: lambda l: 1 if l[0]>l[1] else 0,
        6: lambda l: 1 if l[0]<l[1] else 0,
        7: lambda l: 1 if l[0]==l[1] else 0,
        }

def parse_package(l_bin):

    print("package is: {}".format("".join(l_bin)))
    version = int(l_bin[:3], 2)
    type_id = int(l_bin[3:6], 2)

    if type_id == 4:
        nums, l_bin = parse_literal_num(l_bin[6:])
    else:
        bit_label = int(l_bin[6])
        if bit_label == 0:
            # define the length of total packages
            n_sub_p = int(l_bin[7:7+15], 2)
            select = l_bin[7+15:7+15+n_sub_p]
            l_bin = l_bin[7+15+n_sub_p:]
            print("select 0: total bits of packages: {} = {}, selected: {}, leftover: {}".format("".join(l_bin[7:7+15]), n_sub_p, select, l_bin))
            num_list = []
            while True:
                print("    select 0: {}".format(select))
                v1, t1, n1, select = parse_package(select)
                print("    select 0: leftover {}".format(select))
                num_list.append(n1)
                if len(select) == 0 or all([a=="0" for a in select]):
                    break
            nums = id2fun[type_id](num_list)
            print("list: {} -> {}".format(num_list, nums))
        else:
            # define the number of packages
            n_sub_p = int(l_bin[7:7+11], 2)
            print("select 1: n_packages: {}={}".format("".join(l_bin[7:7+11]), n_sub_p))
            l_bin = l_bin[7+11:]
            num_list = []
            for i_package in range(n_sub_p):
                print("    select 1: package {}: parse {}".format(i_package, l_bin))
                v1, t1, n1, l_bin = parse_package(l_bin)
                print("    select 1: package {}: leftover {}".format(i_package, l_bin))
                num_list.append(n1)
            nums = id2fun[type_id](num_list)

    all_version.append(version)
    return version, type_id, nums, l_bin


# s_hex = "D2FE28"
# s_hex = "38006F45291200"
# s_hex = "EE00D40C823060"
# s_hex = "8A004A801A8002F478"
# s_hex = "620080001611562C8802118E34"
# s_hex = "C0015000016115A2E0802F182340"
# s_hex = "A0016C880162017C3686B18A3D4780"

# s_hex = "C200B40A82"
# s_hex = "04005AC33890"
# s_hex = "880086C3E88112"
# s_hex = "CE00C43D881120"
# s_hex = "D8005AC2A8F0"
# s_hex = "F600BC2D8F"
# s_hex = "9C005AC2F8F0"
# s_hex = "9C0141080250320F1802104A08"

package_bin = hex2bin(s_hex)
print(s_hex, package_bin)
assert 4*len(s_hex) == len(package_bin)
output = parse_package(package_bin)
print(output)

