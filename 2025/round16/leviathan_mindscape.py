import re
from itertools import zip_longest
import math

input = """FACE - VALUE 38
ROW 2 - VALUE 71
ROW 1 - VALUE 57
ROW 3 - VALUE 68
COL 1 - VALUE 52

LURD""".split("\n\n")

input = """FACE - VALUE 38
COL 32 - VALUE 39
COL 72 - VALUE 12
COL 59 - VALUE 56
COL 77 - VALUE 31
FACE - VALUE 43
COL 56 - VALUE 47
ROW 73 - VALUE 83
COL 15 - VALUE 87
COL 76 - VALUE 57

ULDLRLLRU""".split("\n\n")


with open("2025/round16/leviathan_mindscape.txt") as f:
    input = f.read().split("\n\n")

instructions = [re.split(r" - | ", line) for line in input[0].splitlines()]
twists = list(input[1])

# print(instructions)
# print(twists)


class Face:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.absorption = 0
        self.grid = [[1] * self.size for _ in range(self.size)]
        # self.grid = [[col + row * self.size + 1
        #               for col in range(self.size)] for row in range(self.size)]

    def getId(self):
        return self.id

    def getAbsorption(self):
        return self.absorption

    def getDominantSum(self):
        return max(max(sum(line) for line in self.grid),
                   max(sum(line) for line in zip(*self.grid)))

    def update_cell(self, cell, value):
        return (cell + value - 1) % 100 + 1

    def update(self, instr):
        if instr[0] == "FACE":
            value = int(instr[2])
            self.grid = [
                [self.update_cell(cell, value) for cell in row]
                for row in self.grid
            ]
            self.absorption += value * self.size**2

        elif instr[0] == "ROW":
            offset = int(instr[1]) - 1
            value = int(instr[3])
            self.grid[offset] = [
                self.update_cell(cell, value) for cell in self.grid[offset]
            ]
            self.absorption += value * self.size

        elif instr[0] == "COL":
            offset = int(instr[1]) - 1
            value = int(instr[3])
            for row in self.grid:
                row[offset] = self.update_cell(row[offset], value)
            self.absorption += value * self.size

    def rotateCW(self):
        self.grid = [list(row) for row in zip(*self.grid[::-1])]

    def rotateCCW(self):
        self.grid = [list(row) for row in zip(*self.grid)][::-1]

    def rotate180(self):
        self.grid = [row[::-1] for row in self.grid[::-1]]

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)


class Cube:
    def __init__(self, size):
        self.size = size

        self.faces = []
        for i in range(6):
            self.faces.append(Face(i+1, self.size))
        self.current = self.faces[0]
        self.bottom = self.faces[1]
        self.back = self.faces[2]
        self.top = self.faces[3]
        self.left = self.faces[4]
        self.right = self.faces[5]

    def getCurrentFaceId(self):
        return self.current.getId()

    def update(self, instr, full_cube=False):
        if instr[0] == "FACE":
            self.current.update(instr)

        elif instr[0] == "ROW":
            self.current.update(instr)
            if full_cube:
                self.right.update(instr)
                self.back.rotate180()
                self.back.update(instr)
                self.back.rotate180()
                self.left.update(instr)

        elif instr[0] == "COL":
            self.current.update(instr)
            if full_cube:
                self.top.update(instr)
                self.back.update(instr)
                self.bottom.update(instr)

    def twist(self, t):
        if t == "L":
            self.current, self.left, self.back, self.right = self.left, self.back, self.right, self.current
            self.top.rotateCCW()
            self.bottom.rotateCW()
            self.back.rotate180()
            self.left.rotate180()

        elif t == "R":
            self.current, self.right, self.back, self.left = self.right, self.back, self.left, self.current
            self.top.rotateCW()
            self.bottom.rotateCCW()
            self.back.rotate180()
            self.right.rotate180()

        elif t == "D":
            self.current, self.bottom, self.back, self.top = self.bottom, self.back, self.top, self.current
            self.left.rotateCCW()
            self.right.rotateCW()

        elif t == "U":
            self.current, self.top, self.back, self.bottom = self.top, self.back, self.bottom, self.current
            self.left.rotateCW()
            self.right.rotateCCW()

    def __str__(self):
        return "#{}#\n{}{}{}\n#{}#\n#{}#".format(
            self.current.getId(), self.bottom.getId(), self.back.getId(),
            self.top.getId(), self.left.getId(), self.right.getId())

    def getAbsorptions(self):
        return [f.getAbsorption() for f in self.faces]

    def getDominantSums(self):
        return [f.getDominantSum() for f in self.faces]


cube = Cube(80)

for instr, twist in zip_longest(instructions, twists, fillvalue=None):
    cube.update(instr)
    if twist:
        cube.twist(twist)

# part 1
print(math.prod(sorted(cube.getAbsorptions(), reverse=True)[:2]))
# part 2
print(math.prod(sorted(cube.getDominantSums(), reverse=True)))

cube = Cube(80)

for instr, twist in zip_longest(instructions, twists, fillvalue=None):
    cube.update(instr, True)
    if twist:
        cube.twist(twist)

# part 3
print(math.prod(sorted(cube.getDominantSums(), reverse=True)))
