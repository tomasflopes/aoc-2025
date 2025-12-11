from collections import defaultdict
import re
from itertools import combinations
from z3 import Optimize, Int

p2 = 0
with open(0, "r") as f:
    data = [re.findall(r'\[([.#]+)\]\s*((?:\([\d,]+\)\s*)+)\{([\d,]+)\}', line.strip())[0] for line in f.readlines()]

def part1():
  r = 0
  for goal, steps, _ in data:
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

    r += res
  return r

def part2():
  res = 0
  for _, steps, joltage in data:
    steps = [list(map(int, x.split(','))) for x in re.findall(r'\(([\d,]+)\)', steps)]
    joltage = list(map(int, joltage.split(',')))
    presses = Int('presses')
    button_vars = [Int(f"button{i}") for i in range(len(steps))]

    counters_button_lookup = defaultdict(list)
    for i, button in enumerate(steps):
        for index in button:
            counters_button_lookup[index].append(i)

    equations = []

    for counter, counter_buttons in counters_button_lookup.items():
        equations.append(joltage[counter] == sum([button_vars[i] for i in counter_buttons]))

    for button_var in button_vars:
        equations.append(button_var >= 0)

    equations.append(presses == sum(button_vars))

    opt = Optimize()
    opt.add(equations)
    opt.minimize(presses)
    opt.check()

    output = opt.model()[presses]

    res += int(str(output)) 
  return res
  
print("Part 1:", part1())
print("Part 2:", part2())
