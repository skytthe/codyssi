import re

input = """tv8cmj0i2951190z5w44fe205k542l5818ds05ib425h9lj260ud38-l6a06
a586m0eeuqqvt5-k-8434hb27ytha3i75-lw23-0cj856l7zn8234a05eron""".split()


with open("2025/round8/risky_shortcut.txt") as f:
    input = [l.strip() for l in f.readlines()]


# part 1
reg = r"[a-zA-Z]"
sum1 = sum(len(re.findall(reg, line)) for line in input)

print(sum1)

# part 2
regd = r"\d"
sum2 = 0
for line in input:
    digits = len(re.findall(regd, line))
    res = abs(len(line) - 2*digits)
    sum2 += res

print(sum2)


# part 3
sum3 = 0
for line in input:
    tmp = list(line)
    idx = 0
    while idx < len(tmp):
        if tmp[idx].isdigit():
            if idx-1 >= 0 and tmp[idx-1].isalpha():
                tmp.pop(idx)
                tmp.pop(idx-1)
                idx = 0
            elif idx+1 < len(tmp) and tmp[idx+1].isalpha():
                tmp.pop(idx+1)
                tmp.pop(idx)
                idx = 0
            else:
                idx += 1
        else:
            idx += 1
    sum3 += len(tmp)

print(sum3)
