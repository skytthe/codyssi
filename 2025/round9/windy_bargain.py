

input = """Alpha HAS 131
Bravo HAS 804
Charlie HAS 348
Delta HAS 187
Echo HAS 649
Foxtrot HAS 739

FROM Echo TO Foxtrot AMT 328
FROM Charlie TO Bravo AMT 150
FROM Charlie TO Delta AMT 255
FROM Alpha TO Delta AMT 431
FROM Foxtrot TO Alpha AMT 230
FROM Echo TO Foxtrot AMT 359
FROM Echo TO Alpha AMT 269
FROM Delta TO Foxtrot AMT 430
FROM Bravo TO Echo AMT 455
FROM Charlie TO Delta AMT 302""".split("\n\n")

with open("2025/round9/windy_bargain.txt") as f:
    input = f.read().split("\n\n")

init = [line.split() for line in input[0].split("\n")]
transactions = [line.split() for line in input[1].split("\n")]

balances1 = {i[0]: int(i[2]) for i in init}
balances2 = {i[0]: int(i[2]) for i in init}
balances3 = {i[0]: int(i[2]) for i in init}

# part 1
for t in transactions:
    frm = t[1]
    to = t[3]
    amount = int(t[5])
    balances1[frm] -= amount
    balances1[to] += amount


print(sum(sorted(list(balances1.values()))[-3:]))


# part 2
for t in transactions:
    frm = t[1]
    to = t[3]
    amount = int(t[5])
    if balances2[frm] < amount:
        amount = balances2[frm]
    balances2[frm] -= amount
    balances2[to] += amount


print(sum(sorted(list(balances2.values()))[-3:]))


# part 3
debts = {i[0]: [] for i in init}
for t in transactions:
    frm = t[1]
    to = t[3]
    amount = int(t[5])
    if balances3[frm] < amount:
        debt = amount - balances3[frm]
        amount = balances3[frm]
        debts[frm].append([to, debt])
    balances3[frm] -= amount
    balances3[to] += amount

    for _ in range(len(balances3.keys())):
        for to in balances3.keys():
            while debts[to] and balances3[to] > 0:
                k, v = debts[to][0]
                if v > balances3[to]:
                    amount = balances3[to]
                    balances3[to] -= amount
                    balances3[k] += amount
                    debts[to][0][1] -= amount
                    break
                else:
                    debts[to].pop(0)
                    balances3[to] -= v
                    balances3[k] += v

print(sum(sorted(list(balances3.values()))[-3:]))
