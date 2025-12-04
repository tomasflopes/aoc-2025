DIR_8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
data = []
p1 = p2 = 0

def adjacent_8(m, r, c):
    return sum(0 <= r+dr < len(m) and 0 <= c+dc < len(m[0]) and m[r+dr][c+dc] == 1 for dr, dc in DIR_8)

with open(0) as f:
  data = [[1 if x=='@' else 0 for x in line.strip()] for line in f]

p1 = sum(adjacent_8(data,r,c) < 4 and data[r][c] == 1
         for r in range(len(data))
         for c in range(len(data[0])))

changed = True
while changed: 
  changed = False
  for r in range(len(data)):
      for c in range(len(data[0])):
        if adjacent_8(data, r, c) < 4 and data[r][c] == 1:
            p2 += 1
            data[r][c] = 0
            changed = True
    
print("Part 1:", p1)
print("Part 2:", p2)
