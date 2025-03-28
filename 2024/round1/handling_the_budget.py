

input = """912372
283723
294281
592382
721395
91238""".split()

with open("2024/round1/handling_the_budget.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = list(map(int, input))

# part 1
print(sum(input))

# part 2
print(sum(list(reversed(sorted(input)))[20:]))
print(sum(sorted(input, reverse=True)[20:]))

# part 3
print(sum(list(a-b for a, b in zip(input[::2], input[1::2]))))
