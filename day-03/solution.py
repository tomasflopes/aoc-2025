data = []
p1 = p2 = 0

with open(0, "r") as f:
    data = [x.strip() for x in f.readlines()]

def k_largest_right_constrained(line, k):
    line = list(map(int, line))
    chosen = []
    start = 0
    n = len(line)

    for j in range(k):
        remaining = k - j - 1
        
        end = n - remaining  

        best_val = -1
        best_idx = -1

        for i in range(start, end):
            if line[i] > best_val:
                best_val = line[i]
                best_idx = i

        if best_idx == -1:
            break

        chosen.append(best_val)
        start = best_idx + 1

    return chosen

def value_from_digits(digits, k):
    n = 0
    for i, d in enumerate(digits):
        n += d * (10 ** (k - i - 1))
    return n

for line in data:
    numbers = k_largest_right_constrained(line, 2)
    p1 += value_from_digits(numbers, 2)

    numbers = k_largest_right_constrained(line, 12)
    p2 += value_from_digits(numbers, 12)

print("Part 1:", p1)
print("Part 2:", p2)
