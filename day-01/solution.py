data = []
with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]

pos = 50
p1 = p2 = 0

for line in data:
    dir = line[0] == "R" and 1 or -1
    steps = int(line[1:])

    p2 += abs((pos + steps * dir) // 100)
    if dir == -1:
      p2 -= (pos % 100) == 0 
      p2 += (pos + dir * steps) % 100 == 0 
    
    pos = (pos + dir * steps) % 100
    if pos == 0:
        p1 += 1
      
print("Part 1: ", p1)
print("Part 2: ", p2)
