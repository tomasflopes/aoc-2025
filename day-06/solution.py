p1 = p2 = 0

with open(0, "r") as f:
    lines = f.readlines()
    data = [list(map(int, line.strip().split())) for line in lines[:-1]]
    ops = [x for x in lines[-1].strip().split() if x != ""]

ops_p2 = []
for col in range(len(data[0])):
    r = 0
    col_vals = [data[row][col] for row in range(len(data))]
    max_len = max(len(str(v)) for v in col_vals)
    ops_p2.extend([ops[col]] * (max_len+1))
    op = ops[col]
    if op == "*":
        r = 1
        for v in col_vals:
            r *= v
    elif op == "+":
        r = sum(col_vals)
    p1 += r

nums = []
for col in range(len(lines[0])):
    r = 0
    col_vals = [lines[row][col] for row in range(len(lines[:-1]))]
    if all(v == " " or v == "\n" for v in col_vals):
      if ops_p2[col] == "*":
        r = 1
        for v in nums:
            r *= v
      elif ops_p2[col] == "+":
        r = sum(nums)
      nums = []
      p2 += r
      continue

    col_vals = [int(v) if v != " " else 0 for v in col_vals]
    num = 0
    for v in col_vals:
      if v != 0:
        num = num * 10 + v
    nums.append(num)

print("Part 1:", p1)
print("Part 2:", p2)
