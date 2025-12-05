data = []

with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]

ranges = []
ingredients = []
for line in data:
  if line.__contains__("-"):
     ranges.append(list(map(int, line.split("-"))))
  elif line != "":
      ingredients.append(int(line))

fresh = {
    ing for ing in ingredients
    if any(a <= ing <= b for a, b in ranges)
}

intervals = sorted(ranges)

merged = []
for start, end in intervals:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

length = sum(end - start + 1 for start, end in merged)

print("Part 1:", len(fresh))
print("Part 2:", length)
