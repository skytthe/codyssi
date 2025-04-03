import re
from functools import cache

input = """S1 : 0 -> 6 : FROM START TO END
S2 : 2 -> 3 : FROM S1 TO S1

Possible Moves : 1, 3""".split("\n\n")

with open("2025/round17/spiralling_stairs.txt") as f:
    input = f.read().split("\n\n")


stairs = [tuple(map(int, re.findall(r"\d+", line)))
          for line in input[0].splitlines()]

for stair in stairs:
    if stair[0] == 1:
        start_level = stair[1]
        goal_level = stair[2]
    else:
        pass

possible_moves = tuple(map(int, re.findall(r"\d+", input[1])))


@cache
def move(pos, goal, possibleMoves):
    if pos == goal:
        return 1
    elif pos > goal:
        return 0
    else:
        moves = 0
        for m in possibleMoves:
            moves += move(pos+m, goal, possibleMoves)
        return moves


print(move(start_level, goal_level, possible_moves))


# print(move(0, 6, (1, 3)))
# print(move(0, 6, (1, 2)))
# print(move(0, 99, (1, 3, 5, 6)))
# print(move(0, 98, (1, 2, 3, 5, 7)))
