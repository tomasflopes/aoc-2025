from shapely import Polygon
p2 = 0

with open(0, "r") as f:
    data = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

areas = {}
poly = Polygon(data)
for x, y in data:
    for xx, yy in data:
        areas[(x, y, xx, yy)] = (abs(xx - x) + 1) * (abs(yy - y) + 1)
        curr = Polygon(((min(x, xx), min(y, yy)), (max(x, xx), min(y, yy)), (max(x, xx), max(y, yy)), (min(x, xx), max(y, yy))))
        if poly.contains(curr) and areas[(x, y, xx, yy)] > p2:
            p2 = areas[(x, y, xx, yy)]
              
areas = dict(sorted(areas.items(), key=lambda item: item[1], reverse=True))
print("Part 1:", list(areas.values())[0])
print("Part 2:", p2)
