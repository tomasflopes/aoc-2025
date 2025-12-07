data = []
p1 = 0

with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]

start = len(data[0]) // 2
pos = {start}
for line in data[1:]:
  temp = set()
  for p in pos:
      if line[p] == "^":
          p1 += 1
          temp.update({p - 1, p + 1})
      else:
          temp.add(p)
  pos = temp

pos = {start: 1}
for line in data[1:]:
  temp = {}
  for p, count in pos.items():
      if line[p] == "^":
          temp[p - 1] = temp.get(p - 1, 0) + count
          temp[p + 1] = temp.get(p + 1, 0) + count
      else:
          temp[p] = temp.get(p, 0) + count
  pos = temp

print("Part 1:", p1)
print("Part 2:", sum(pos.values()))
