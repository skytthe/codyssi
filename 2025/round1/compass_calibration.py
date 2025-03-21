
input = """8
1
5
5
7
6
5
4
3
1
-++-++-++""".split("\n")

digits = []
ops = []


with open("2025/round1/compass_calibration.txt") as f:
    input = [l.strip() for l in f.readlines()]


for line in input:
    if line.isdigit():
        digits.append(int(line))
    else:
        ops = [ch for ch in line]

# print(digits)
# print(ops)

total = digits[0]
for d, op in zip(digits[1:], ops):
    if op == "+":
        total += d
    else:
        total -= d

print(total)

ops.reverse()

total2 = digits[0] + sum(d if op == "+" else -d for d,
                         op in zip(digits[1:], ops))

print(total2)

total3 = digits[0]*10 + digits[1]
for i, op in zip(range(2, len(digits), 2), ops):
    sign = 1
    if op == "-":
        sign = -1

    total3 += sign * (digits[i]*10 + digits[i+1])

print(total3)
