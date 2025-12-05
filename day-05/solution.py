with open(0, "r") as f:
    lines = f.readlines()
    ranges, ingredients = (
        [list(map(int, line.split("-"))) for line in lines if "-" in line],
        [int(line) for line in lines if line.strip() != "" and "-" not in line],
    )

fresh = {
    ing for ing in ingredients
    if any(a <= ing <= b for a, b in ranges)
}

merged = []
intervals = sorted(ranges)
for start, end in intervals:
    if merged == [] or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

print("Part 1:", len(fresh))
print("Part 2:", sum(end - start + 1 for start, end in merged))
