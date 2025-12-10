import re
from itertools import combinations
p1 = p2 = 0
# regex to find this [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7} in each line
with open(0, "r") as f:
    data = [re.findall(r'\[([.#]+)\]\s*((?:\([\d,]+\)\s*)+)\{([\d,]+)\}', line.strip())[0] for line in f.readlines()]

for goal, steps, joltage in data:
  steps = [list(map(int, x.split(','))) for x in re.findall(r'\(([\d,]+)\)', steps)]
  res = 0
  for n in range(1, len(steps)):
    found = False
    for s in combinations(steps, n):
      curr = "."*len(goal)
      for combo in s:
        for i in combo:
            if curr[i] == '#':
              curr = curr[:i] + '.' + curr[i+1:]
            else:
              curr = curr[:i] + '#' + curr[i+1:]
      if goal == curr:
          found = True
          res = max(res, n)
          break
    if found:
        break

  p1 += res
print("Part 1:", p1)
print("Part 2:", p2)
