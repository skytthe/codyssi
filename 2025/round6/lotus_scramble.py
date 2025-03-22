import re

input = "t#UD$%%DVd*L?^p?S$^@#@@$pF$?xYJ$LLv$@%EXO&$*iSFZuT!^VMHy#zKISHaBj?e*#&yRVdemc#?&#Q%j&ev*#YWRi@?mNQ@eK".split()

with open("2025/round6/lotus_scramble.txt") as f:
    input = [l.strip() for l in f.readlines()]

# part 1
reg = r"[a-zA-Z]"
uncorrupted_data = re.findall(reg, input[0])

print(len(uncorrupted_data))


# part 2
total_sum2 = sum(ord(ch) - 96 if ch.islower() else ord(ch) -
                 64 + 26 for ch in uncorrupted_data)

print(total_sum2)


# part 3
data = list(input[0])
reconstructed_data = []
for ch in data:
    if ch.isalpha():
        value = ord(ch) - 96 if ch.islower() else ord(ch) - 64 + 26
        reconstructed_data.append(value)
    else:
        new_value = (reconstructed_data[-1] * 2 - 5) % 52
        reconstructed_data.append(new_value)

print(sum(reconstructed_data))
