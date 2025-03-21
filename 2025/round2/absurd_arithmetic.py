

input = """Function A: ADD 495
Function B: MULTIPLY 55
Function C: RAISE TO THE POWER OF 3

5219
8933
3271
7128
9596
9407
7005
1607
4084
4525
5496""".split("\n")

with open("2025/round2/absurd_arithmetic.txt") as f:
    input = [l.strip() for l in f.readlines()]


func_a = int(input[0].split()[-1])
func_b = int(input[1].split()[-1])
func_c = int(input[2].split()[-1])

room_qualities = [int(s) for s in input[4:]]

room_qualities.sort()

median = room_qualities[len(room_qualities)//2]

ep_price = (median**func_c)*func_b+func_a

print(ep_price)

# part 2
room_sum = sum(p if p % 2 == 0 else 0 for p in room_qualities)

ep_price2 = (room_sum**func_c)*func_b+func_a

print(ep_price2)

# part 3
max_price = 15000000000000
room_quality = 0
for rq in room_qualities:
    price = (rq**func_c)*func_b+func_a
    if price <= max_price:
        room_quality = rq
    else:
        break

print(room_quality)

room_quality = max(rq for rq in room_qualities if (
    rq**func_c)*func_b+func_a <= max_price)

print(room_quality)
