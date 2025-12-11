from functools import lru_cache
p1 = 0
p2 = []

with open(0, "r") as f:
    data = [line.strip().replace(":", "").split() for line in f.readlines()]
m = {r[0]: r[1:] for r in data}
m["out"] = []

def dfs(node, out, visited=set()): 
  global p1 
  if node == out: 
    p1 += 1 
    return
  for neighbor in m[node]: 
    if neighbor not in visited: 
      dfs(neighbor, out, visited | {neighbor})

# dfs("you", "out")
# print("Part 1:", p1)

@lru_cache(None)
def count_paths(start, end):
    if start == end:
        return 1
    total = 0
    for nxt in m[start]:
        total += count_paths(nxt, end)
    return total

# Required intermediate nodes
a, b = "dac", "fft"

# Case 1: svr -> dac -> fft -> out
case1 = (
    count_paths("svr", a) *
    count_paths(a, b) *
    count_paths(b, "out")
)

# Case 2: svr -> fft -> dac -> out
case2 = (
    count_paths("svr", b) *
    count_paths(b, a) *
    count_paths(a, "out")
)

print("Total valid paths:", case1 + case2)
