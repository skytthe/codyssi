from collections import defaultdict

input = """ADB <-> XYZ
STT <-> NYC
PLD <-> XYZ
ADB <-> NYC
JLI <-> NYC
PTO <-> ADB""".split("\n")

with open("2024/round4/traversing_the_country.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = [l.split(" <-> ") for l in input]

# part 1
print(len(set(e for l in input for e in l)))


# part 2
net = defaultdict(list)
for a, b in input:
    net[a].append(b)
    net[b].append(a)

visited = set(["STT"])
for _ in range(3):
    tmp = []
    for e in visited:
        tmp += net[e]
    visited.update(tmp)
print(len(visited))


# part 3
visited = set(["STT"])
dist = {"STT": 0}
h = 0
while len(visited) < 50:
    h += 1
    tmp = []
    for e in visited:
        for n in net[e]:
            if n not in dist:
                dist[n] = h
            tmp.append(n)
    visited.update(tmp)
print(sum(dist.values()))
