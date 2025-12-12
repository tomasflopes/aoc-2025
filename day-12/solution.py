with open(0, "r") as f:
    data = [x.split("\n") for x in [line.strip() for line in f.read().split("\n\n")]]
    shapes = ["".join(x[1:]).count("#") for x in data[:-1]]
    regions = [{"dimensions": tuple(map(int, x.split(":")[0].strip().split("x"))), "points": [int(point.strip()) for point in x.split(":")[1].strip().split()]} for x in data[-1]]

print("Part 1:", sum(1 for region in regions if sum(quant * shapes[i] for i, quant in enumerate(region["points"])) < region["dimensions"][0] * region["dimensions"][1]))
