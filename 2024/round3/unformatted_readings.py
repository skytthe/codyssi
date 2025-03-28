

input = """100011101111110010101101110011 2
83546306 10
1106744474 8
170209FD 16
2557172641 8
2B290C15 16
279222446 10
6541027340 8""".split("\n")

with open("2024/round3/unformatted_readings.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = [l.split(" ") for l in input]


# part 1
print(sum(map(int, list(zip(*input))[1])))


# part 2
print(sum(int(n, int(base)) for n, base in input))


# part 3
def number2char65(n):
    s = list("0123456789") + [chr(i+65) for i in range(26)] + \
        [chr(i+97) for i in range(26)] + list("!@#")
    return s[n]


def toBase65(n: int) -> str:
    if n == 0:
        return "0"

    res = ""
    while n > 0:
        res = number2char65(n % 65) + res
        n = n // 65
    return res


print(toBase65(sum(int(n, int(base)) for n, base in input)))
