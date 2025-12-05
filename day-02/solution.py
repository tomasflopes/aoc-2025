p1 = p2 = 0

with open(0, "r") as f:
    ranges = [(int(x), int(y)) for x, y in [r.split("-") for r in f.readline().strip().split(",")]]

def is_invalid_p1(s):
    return s[:len(s) // 2] == s[len(s) // 2:]

def is_invalid_p2(s):
    for group_len in range(1, len(s) // 2 + 1):
        if s[:group_len] * (len(s) // group_len) == s: return True
    return False

for start, end in ranges:
    for i in range(start, end + 1):
        if is_invalid_p1(str(i)): p1 += i
        if is_invalid_p2(str(i)): p2 += i

print("Part 1:", p1)
print("Part 2:", p2)
