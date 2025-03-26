import queue


input = """33178413177678782771
99763694926457393756
89767732278971531244
92823592657816736796
41752276872392216275
29129912293745337194
99526623183336798315
84872179873791852528
68966422777812626167
38869927854188583566
28726847176894312898
62977287956682844822
31288468914391422154
52672739217612421159
36894477334861297296
94557417713238176319
53831153159236644853
63829736432869812715
41248771874457233833
15733515411192146563""".split("\n")


with open("2025/round10/cyclops_chaos.txt") as f:
    input = f.read().split("\n")


grid = [list(map(int, line)) for line in input]
grid_t = list(zip(*grid))

res = 10000000
for i in range(len(grid)):
    res = min(sum(grid[i]), res)
    res = min(sum(grid_t[i]), res)

print(res)


# part 2
x, y = 0, 0
gx, gy = 14, 14

pq = queue.PriorityQueue()
pq.put((grid[y][x], x, y))

visited = set()

while not pq.empty():
    cost, x, y,  = pq.get()
    visited.add((x, y))
    if x == gx and y == gy:
        print(cost)
        break

    if (x+1, y) not in visited and x+1 < len(grid[0]):
        pq.put((cost+grid[y][x+1], x+1, y))
    if (x, y+1) not in visited and y+1 < len(grid):
        pq.put((cost+grid[y+1][x], x, y+1))

# part 3
x, y = 0, 0
gx, gy = 49, 49

pq = queue.PriorityQueue()
pq.put((grid[y][x], x, y))

visited = set()

while not pq.empty():
    cost, x, y,  = pq.get()
    visited.add((x, y))
    if x == gx and y == gy:
        print(cost)
        break

    if (x+1, y) not in visited and x+1 < len(grid[0]):
        pq.put((cost+grid[y][x+1], x+1, y))
    if (x, y+1) not in visited and y+1 < len(grid):
        pq.put((cost+grid[y+1][x], x, y+1))
