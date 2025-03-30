import re
from collections import defaultdict
import queue
import math

input = """STT -> MFP | 5
AIB -> ZGK | 6
ZGK -> KVX | 20
STT -> AFG | 4
AFG -> ZGK | 16
MFP -> BDD | 13
BDD -> AIB | 5
AXU -> MFP | 4
CLB -> BLV | 20
AIB -> BDD | 13
BLV -> AXU | 17
AFG -> CLB | 2""".split("\n")

with open("2025/round13/laestrygonian_guards.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = [re.findall(r"\w+", s) for s in input]

net = defaultdict(list)
path_cost = dict()
for a, b, c in input:
    net[a].append(b)
    path_cost[(a, b)] = int(c)


# part 1
pq = queue.PriorityQueue()
dist = dict()
start = "STT"
pq.put((0, start))

while not pq.empty():
    cost, location = pq.get()
    dist[location] = cost
    next = net[location]
    for nl in next:
        if nl not in dist:
            pq.put((cost+1, nl))

print(math.prod(sorted(dist.values(), reverse=True)[:3]))

# part 2
pq = queue.PriorityQueue()
dist = dict()
start = "STT"
pq.put((0, start))
while not pq.empty():
    cost, location = pq.get()
    dist[location] = cost
    next = net[location]
    for nl in next:
        if nl not in dist:
            pq.put((cost+path_cost[(location, nl)], nl))

print(math.prod(sorted(dist.values(), reverse=True)[:3]))


# part 3
all_dist = dist.keys()

max_dist = []
for start in all_dist:
    stack = [(0, start)]
    dist = {}

    while stack:
        cost, location = stack.pop()
        if location not in dist:
            dist[location] = cost

            next = net[location]
            for nl in next:
                if nl not in dist:
                    stack.append((cost + path_cost[(location, nl)], nl))
                if nl == start:
                    max_dist.append(cost + path_cost[(location, nl)])

print(sorted(max_dist, reverse=True)[0])
