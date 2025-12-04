data = []
p1 = p2 = 0
DIR_8 = [(-1, -1), (-1, 0), (-1, 1),
          (0, -1),          (0, 1),
          (1, -1),  (1, 0), (1, 1)]

def print_matrix(matrix):
    for row in matrix:
        print(''.join(['@' if x == 1 else 'x' if x == 2 else '.' for x in row]))
    print()

def adjacent_8(matrix, r, c):
    count = 0
    for dr, dc in DIR_8:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] == 1:
            count += 1
    return count

with open(0, "r") as f:
    data = [[1 if x == '@' else 0 for x in line.strip()] for line in f.readlines()]

for r in range(len(data)):
    for c in range(len(data[0])):
      if adjacent_8(data, r, c) < 4 and data[r][c] == 1:
          p1 += 1

last = p2
while True: 
  for r in range(len(data)):
      for c in range(len(data[0])):
        if adjacent_8(data, r, c) < 4 and data[r][c] == 1:
            p2 += 1
            data[r][c] = 0

  if last == p2:
      break
  last = p2
    
print_matrix(data)
print("Part 1:", p1)
print("Part 2:", p2)
