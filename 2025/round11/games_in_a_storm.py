

input = """32IED4E6L4 22
1111300022221031003013 4
1C1117A3BA88 13
1100010000010010010001111000000010001100101 2
7AJ5G2AB4F 22
k6IHxTD 61""".split("\n")


with open("2025/round11/games_in_a_storm.txt") as f:
    input = [l.strip() for l in f.readlines()]

lines = [l.split(" ") for l in input]


def char2number(ch):
    # 0 to 9, the uppercase characters from A to Z represent numbers 10 to 35, and the lowercase characters from a to z represent numbers 36 to 61
    if ch.isdigit():
        return int(ch)
    if "A" <= ch <= "Z":
        return ord(ch) - 55
    if "a" <= ch <= "z":
        return ord(ch) - 61


nums = []

for n, base in lines:
    res = 0
    for p, d in enumerate(reversed(n)):
        res += char2number(d) * pow(int(base), p)
    nums.append(res)

print(max(nums))


# part 2

def number2char(n):
    # 0 to 9, the uppercase characters from A to Z represent numbers 10 to 35, and the lowercase characters from a to z represent numbers 36 to 61
    if n < 10:
        return str(n)
    elif 10 <= n <= 35:
        return chr(n+55)
    elif 36 <= n <= 61:
        return chr(n+61)
    # ! represents 62, @ represents 63, # represents 64, $ represents 65, % represents 66, and ^ represents 67.
    elif n == 62:
        return '!'
    elif n == 63:
        return '@'
    elif n == 64:
        return '#'
    elif n == 65:
        return '$'
    elif n == 66:
        return '%'
    elif n == 67:
        return '^'


def number2char68(n):
    s = list("0123456789") + [chr(i+65) for i in range(26)] + \
        [chr(i+97) for i in range(26)] + list("!@#$%^")
    return s[n]


def base10_to_base68(n):
    if n == 0:
        return "0"

    res = ""
    while n > 0:
        remainder = n % 68
        res = number2char68(remainder) + res
        n = n // 68

    return res


sum_of_nums = sum(nums)
print(base10_to_base68(sum_of_nums))


# part 3
base = 10
while pow(base, 4) <= sum_of_nums:
    base += 1

print(base)
