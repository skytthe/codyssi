from itertools import chain
import re

input = """8-9 9-10
7-8 8-10
9-10 5-10
3-10 9-10
4-8 7-9
9-10 2-7"""

with open("2025/round3/supplies_in_surplus.txt") as f:
    input = f.read()
input1 = input.split()
input2 = input.split("\n")

# part 1
box_sum1 = sum(-1*eval(line) + 1 for line in input1)

print(box_sum1)


# part 2
box_sum2 = 0
reg = r'\d+'
for line in input2:
    tmp = list(map(int, re.findall(reg, line)))
    r1 = range(tmp[0], tmp[1]+1)
    r2 = range(tmp[2], tmp[3]+1)
    combined_range = set(chain(r1, r2))
    box_sum2 += len(combined_range)

print(box_sum2)


# part 3
max_box_sum = 0
for line in zip(input2[:-1], input2[1:]):
    tmp0 = list(map(int, re.findall(reg, line[0])))
    tmp1 = list(map(int, re.findall(reg, line[1])))
    r1 = range(tmp0[0], tmp0[1]+1)
    r2 = range(tmp0[2], tmp0[3]+1)
    r3 = range(tmp1[0], tmp1[1]+1)
    r4 = range(tmp1[2], tmp1[3]+1)
    combined_range = set(chain(r1, r2, r3, r4))
    max_box_sum = max(max_box_sum, len(combined_range))

print(max_box_sum)
