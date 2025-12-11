import re
from collections import defaultdict
from itertools import combinations
from z3 import Optimize, Int

with open(0, "r") as f:
    data = [re.findall(r'\[([.#]+)\]\s*((?:\([\d,]+\)\s*)+)\{([\d,]+)\}', line.strip())[0] for line in f.readlines()]

def part1():
  r = 0
  for goal, steps, _ in data:
    steps = [list(map(int, x.split(','))) for x in re.findall(r'\(([\d,]+)\)', steps)]
    res = 0
    for n in range(1, len(steps)):
      for s in combinations(steps, n):
        curr = ["."]*len(goal)
        for combo in s:
          for i in combo:
              curr[i] = '#' if curr[i] == '.' else '.'
        if goal == "".join(curr):
            res = max(res, n)
            break
      if res != 0:
          break
    r += res
  return r

def part2():
  res = 0
  for _, steps, joltage in data:
    steps = [list(map(int, x.split(','))) for x in re.findall(r'\(([\d,]+)\)', steps)]
    joltage = list(map(int, joltage.split(',')))
    presses = Int('presses')
    button_vars = [Int(f"button{i}") for i in range(len(steps))]

    button_counter = defaultdict(list)
    for i, button in enumerate(steps):
        for index in button:
            button_counter[index].append(i)

    equations = [joltage[idx] == sum(button_vars[b] for b in btns) for idx, btns in button_counter.items()]
    equations += [var >= 0 for var in button_vars]
    equations.append(presses == sum(button_vars))

    opt = Optimize()
    opt.add(equations)
    opt.minimize(presses)
    opt.check()
    res += int(str(opt.model()[presses]))

  return res
  
print("Part 1:", part1())
print("Part 2:", part2())
