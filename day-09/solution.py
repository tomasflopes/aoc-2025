p1 = p2 = 0

with open(0, "r") as f:
    data = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

areas = {}
for x, y in data:
    for xx, yy in data:
        areas[(x, y, xx, yy)] = (abs(xx - x) + 1) * (abs(yy - y) + 1)
              
areas = dict(sorted(areas.items(), key=lambda item: item[1], reverse=True))
print("Part 1:", list(areas.values())[0])
print("Part 2:", p2)
