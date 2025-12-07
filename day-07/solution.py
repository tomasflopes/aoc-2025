with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]

pos = {len(data[0])//2: 1}
p1 = 0

for line in data[2:]:
  temp = {}
  for p, count in pos.items():
      if line[p] == "^":
          temp[p - 1] = temp.get(p - 1, 0) + count
          temp[p + 1] = temp.get(p + 1, 0) + count
          p1 += 1
      else:
          temp[p] = temp.get(p, 0) + count
  pos = temp

print("Part 1:", p1)
print("Part 2:", sum(pos.values()))
