with open(0, "r") as f:
    data = [list(map(int, x.strip())) for x in f.readlines()]

def k_largest(line, k):
    res = []
    start = 0

    for j in range(k):
        end = len(line) - k + j + 1
        best_val = max(line[start:end])
        best_idx = start + line[start:end].index(best_val)

        res.append(best_val)
        start = best_idx + 1

    return sum(d * (10 ** (len(res) - i - 1)) for i, d in enumerate(res))

print("Part 1:", sum(k_largest(line, 2) for line in data))
print("Part 2:", sum(k_largest(line, 12) for line in data))
