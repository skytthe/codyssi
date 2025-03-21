import re

input = """(-16, -191)
(92, 186)
(157, -75)
(39, -132)
(-42, 139)
(-74, -150)
(200, 197)
(-106, 105)""".split("\n")

with open("2025/round5/patron_islands.txt") as f:
    input = [l.strip() for l in f.readlines()]

reg = r"-?\d+"

xy = list(tuple(map(int, re.findall(reg, line))) for line in input)

ship_pos = (0, 0)
dists = []
for x, y in xy:
    d = abs(x) + abs(y)
    dists.append(d)

dists.sort()

print(dists[-1]-dists[0])

# part 2
sorted_xy = sorted(xy, key=lambda t: (
    abs(t[0]) + abs(t[1]), abs(t[0]), abs(t[1])))

nx, ny = sorted_xy[0]
sorted_xy = sorted(xy, key=lambda t: (
    abs(nx-t[0]) + abs(ny-t[1]), abs(t[0]), abs(t[1])))

print(abs(sorted_xy[0][0]-sorted_xy[1][0]) +
      abs(sorted_xy[0][1]-sorted_xy[1][1]))

# part 3
cx, cy = 0, 0
traveled_dist = 0

while len(xy) > 0:
    xy = sorted(xy, key=lambda t: (
        abs(cx-t[0]) + abs(cy-t[1]), abs(t[0]), abs(t[1])))

    nx, ny = xy.pop(0)
    # print(f"{nx},{ny}")
    traveled_dist += abs(cx-nx) + abs(cy-ny)
    cx, cy = nx, ny

print(traveled_dist)
