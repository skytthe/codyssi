from itertools import combinations
import re
import pprint
from itertools import permutations

input = """"1 ETdhCGi | Quality : 36, Cost : 25, Unique Materials : 7
2 GWgcpkv | Quality : 38, Cost : 17, Unique Materials : 25
3 ODVdJYM | Quality : 1, Cost : 1, Unique Materials : 26
4 wTdbhEr | Quality : 23, Cost : 10, Unique Materials : 18
5 hoOYtHQ | Quality : 25, Cost : 15, Unique Materials : 27
6 jxRouXI | Quality : 31, Cost : 17, Unique Materials : 7
7 dOXpCyA | Quality : 23, Cost : 2, Unique Materials : 28
8 LtCtwHO | Quality : 37, Cost : 26, Unique Materials : 29
9 DLxTAif | Quality : 32, Cost : 24, Unique Materials : 1
10 XCUJAZF | Quality : 22, Cost : 25, Unique Materials : 29
11 cwoqgJA | Quality : 38, Cost : 28, Unique Materials : 7
12 ROPdFSh | Quality : 41, Cost : 29, Unique Materials : 15
13 iYypXES | Quality : 37, Cost : 12, Unique Materials : 15
14 srwmKYA | Quality : 48, Cost : 25, Unique Materials : 14
15 xRbzjOM | Quality : 36, Cost : 20, Unique Materials : 21""".splitlines()

with open("2025/round14/crucial_crafting.txt") as f:
    input = [l.strip() for l in f.readlines()]

input = [line.replace(",", "").split() for line in input]
input = [[line[i] if i == 1 else int(line[i])
          for i in [1, 5, 8, 12]] for line in input]

# part 1
pprint.pp(sum([i[3]
          for i in sorted(input, key=lambda t: (t[1], t[2], t[3]), reverse=True)[:5]]))


# part 2
def powerset(pset, elements):
    if not elements:
        return pset
    e = elements[0]
    tmp = list()
    for s in pset:
        cost = sum([i[2] for i in s + (e,)])
        if cost <= 30:
            tmp.append(s + (e,))
    return powerset(pset + tmp, elements[1:])


pset = powerset([()], input)

values = []
for s in pset:
    total_quality = sum([i[1] for i in s])
    unique_materials = sum([i[3] for i in s])
    # cost = sum([i[2] for i in s])
    res = total_quality * unique_materials
    values.append((total_quality, res))


print(sorted(values, reverse=True)[0][1])


# part 3
def knapsack(items, max_price):
    n = len(items)
    dp = [[0] * (max_price + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        id, quality, cost, materials = items[i - 1]
        for w in range(max_price + 1):
            if cost > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + quality)

    w = max_price
    best_quality = dp[n][w]
    best_combination = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            id, quality, cost, materials = items[i - 1]
            best_combination.append(items[i - 1])
            w -= cost

    return best_quality, best_combination


cost = 300
best_quality, best_items = knapsack(input, cost)

total_quality = sum([i[1] for i in best_items])
unique_materials = sum([i[3] for i in best_items])
print(total_quality * unique_materials)
