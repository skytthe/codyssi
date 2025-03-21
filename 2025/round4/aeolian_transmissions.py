

input = """NNBUSSSSSDSSZZZZMMMMMMMM
PWAAASYBRRREEEEEEE
FBBOFFFKDDDDDDDDD
VJAANCPKKLZSSSSSSSSS
NNNNNNBBVVVVVVVVV""".split()

# input = """ABCDEFGHIJ
# OONNHHHHHANNNHHHHHHHH
# BDGGGSCLUUVLCBBBQNUUUFFFFFXXXXXXXXX""".split()

with open("2025/round4/aeolian_transmissions.txt") as f:
    input = [l.strip() for l in f.readlines()]

total_sum1 = sum((ord(ch)-64) for line in input for ch in line)

print(total_sum1)


# part 2
lossy_compressed_lines = []
for line in input:
    keep = len(line) // 10
    s = line[0:keep] + str(len(line) - 2 * keep) + line[-(keep):]
    lossy_compressed_lines.append(s)

# for line in compressed_lines:
#     print(line)
#     print(sum((ord(ch)-64) if ord(ch) > 64 else int(ch)
#               for ch in line))


total_sum2 = sum((ord(ch)-64) if ord(ch) > 64 else int(ch)
                 for line in lossy_compressed_lines for ch in line)

print(total_sum2)


# part 3
lossless_compressed_lines = []
for line in input:
    idx = 1
    new_line = ""
    count = 1
    last_char = line[0]
    while idx < len(line):
        if line[idx] == last_char:
            count += 1

        else:
            new_line = new_line + str(count) + last_char
            count = 1
        last_char = line[idx]
        idx += 1
    new_line = new_line + str(count) + last_char
    lossless_compressed_lines.append(new_line)

total_sum3 = sum((ord(ch)-64) if ord(ch) > 64 else int(ch)
                 for line in lossless_compressed_lines for ch in line)

print(total_sum3)


# total_sum = sum(
#     (ord(ch) - 64 if ord(ch) > 64 else int(ch))
#     for line in (
#         ''.join(f'{len(list(g))}{k}' for k, g in groupby(line))
#         for line in input
#     )
#     for ch in line
# )
# print(total_sum)


# print(sum(
#     (ord(ch) - 64 if ch.isalpha() else int(ch))
#     for line in (f"{len(list(g))}{k}" for line in input for k, g in groupby(line))
#     for ch in line
# ))
