from itertools import zip_longest
import math

input = """TRUE
FALSE
TRUE
FALSE
FALSE
FALSE
TRUE
TRUE""".split("\n")


with open("2024/round2/sensors_and_circuits.txt") as f:
    input = [line.strip() for line in f.readlines()]

data = [1 if l == "TRUE" else 0 for l in input]


# part 1
print(sum([data[i]*(i+1) for i in range(len(data))]))


# part 2
print(sum((a and b) + (c or d)
      for a, b, c, d in zip(data[::4], data[1::4], data[2::4], data[3::4])))


# part 3
layers = [data]
for i in range(int(math.log2(len(data)))):
    tmp = []
    for a, b, c, d in zip_longest(layers[-1][::4], layers[-1][1::4], layers[-1][2::4], layers[-1][3::4], fillvalue=0):
        tmp.append(a and b)
        tmp.append(c or d)
    layers.append(tmp)
print(sum(sum(l) for l in layers))
