import operator

input = """222 267 922 632 944
110 33 503 758 129
742 697 425 362 568
833 408 425 349 631
874 671 202 430 602

SHIFT COL 2 BY 1
MULTIPLY 4 COL 5
SUB 28 ALL
SHIFT COL 4 BY 2
MULTIPLY 4 ROW 4
ADD 26 ROW 3
SHIFT COL 4 BY 2
ADD 68 ROW 2

TAKE
CYCLE
TAKE
ACT
TAKE
CYCLE""".split("\n\n")

with open("2025/round12/challenging_the_whirlpool.txt") as f:
    input = f.read().split("\n\n")


grid1 = [list(map(int, line.split()))
         for line in input[0].strip().splitlines()]
grid2 = [list(map(int, line.split()))
         for line in input[0].strip().splitlines()]
grid3 = [list(map(int, line.split()))
         for line in input[0].strip().splitlines()]


instructions1 = [line.split() for line in input[1].strip().splitlines()]
instructions2 = [line.split() for line in input[1].strip().splitlines()]
instructions3 = [line.split() for line in input[1].strip().splitlines()]

flow_control = input[2].split()


def shift_op(param, grid):
    # {ROW/COL} {number} BY {shift amount}
    offset = int(param[1])-1
    n = int(param[3])

    if param[0] == 'COL':
        grid = [list(row) for row in zip(*grid)]

    grid[offset] = grid[offset][-n:] + grid[offset][:-n]

    if param[0] == 'COL':
        grid = [list(row) for row in zip(*grid)]

    return grid


def math_op(param, grid):
    oprs = {"ADD": operator.add,
            "SUB": operator.sub,
            "MULTIPLY": operator.mul
            }

    opr = oprs[param[0]]
    value = int(param[1])

    if param[-1] == 'ALL':
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                grid[r][c] = opr(grid[r][c], value) % 1073741824
    else:
        offset = int(param[3])-1
        # transpose
        if param[2] == 'COL':
            grid = [list(row) for row in zip(*grid)]

        for i in range(len(grid[offset])):
            grid[offset][i] = opr(grid[offset][i], value) % 1073741824

        # transpose back
        if param[2] == 'COL':
            grid = [list(row) for row in zip(*grid)]

    return grid


# part 1
for stp, instr in enumerate(instructions1):
    if instr[0] == 'SHIFT':
        grid1 = shift_op(instr[1:], grid1)
    else:
        grid1 = math_op(instr, grid1)

print(max(max(sum(line) for line in grid1),
          max(sum(line) for line in zip(*grid1))))


# part 2
instr = ""
for stp, ctrl_cmd in enumerate(flow_control):
    if ctrl_cmd == "TAKE":
        instr = instructions2.pop(0)
    if ctrl_cmd == "CYCLE":
        instructions2.append(instr)
    if ctrl_cmd == "ACT":
        if instr[0] == 'SHIFT':
            grid2 = shift_op(instr[1:], grid2)
        else:
            grid2 = math_op(instr, grid2)

print(max(max(sum(line) for line in grid2),
          max(sum(line) for line in zip(*grid2))))

# part 3
step = 0
instr = ""
while instructions3:
    ctrl_cmd = flow_control[step % len(flow_control)]

    if ctrl_cmd == "TAKE":
        instr = instructions3.pop(0)
    if ctrl_cmd == "CYCLE":
        instructions3.append(instr)
    if ctrl_cmd == "ACT":
        if instr[0] == 'SHIFT':
            grid3 = shift_op(instr[1:], grid3)
        else:
            grid3 = math_op(instr, grid3)

    step += 1

print(max(max(sum(line) for line in grid3),
          max(sum(line) for line in zip(*grid3))))
