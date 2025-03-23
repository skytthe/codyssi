input = """159
527
827
596
296
413
45
796
853
778

4-8
5-8
10-1
6-5
2-1
6-5
8-7
3-6
7-8
2-10
6-4
8-10
1-9
3-6
7-10

10""".split("\n\n")

with open("2025/round7/siren_disruption.txt") as f:
    input = f.read().split("\n\n")

freq1 = list(map(int, input[0].split()))
freq2 = list(map(int, input[0].split()))
freq3 = list(map(int, input[0].split()))
swap = list(tuple(map(int, s.split("-"))) for s in input[1].split())
test = int(input[2])

# print(freq)
# print(swap)
# print(test)

for a, b in swap:
    freq1[a-1], freq1[b-1] = freq1[b-1], freq1[a-1]

print(freq1[test-1])

# part 2
for a, b in zip(swap, swap[1:] + swap[:1]):
    x, y = a
    z, _ = b
    freq2[y-1], freq2[z-1], freq2[x-1] = freq2[x-1], freq2[y-1], freq2[z-1]

print(freq2[test-1])


# part 3
for a, b in swap:
    x, y = (a, b) if a < b else (b, a)
    l = min(y-x, len(freq3)+1-y)
    freq3[y-1:y-1+l], freq3[x-1:x-1+l] = freq3[x-1:x-1+l], freq3[y-1:y-1+l]

print(freq3[test-1])
