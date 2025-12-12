p1 = p2 = 0

with open(0, "r") as f:
    data = [x.split("\n") for x in [line.strip() for line in f.read().split("\n\n")]]
    shapes = ["".join(x[1:]).count("#") for x in data[:-1]]
    regions = [{"dimensions": list(map(int, x.split(":")[0].strip().split("x"))), "points": [int(point.strip()) for point in x.split(":")[1].strip().split()]} for x in data[-1]]

for region in regions:
    height, width = region["dimensions"]
    points = region["points"]
    c = 0
    for quant, shape in zip(points, shapes):
        c += quant * shape

    print(c, height * width)
    if c < height * width:
        p1 += 1
print("Part 1:", p1)
print("Part 2:", p2)
