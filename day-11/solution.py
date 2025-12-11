from functools import cache

with open(0, "r") as f:
    data = {r[0]: r[1:] for r in [line.strip().replace(":", "").split() for line in f.readlines()]}
    data["out"] = []

@cache
def count_paths(start, end):
    if start == end: return 1
    return sum(count_paths(nxt, end) for nxt in data[start])

dac_fft = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
fft_dac = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")

print("Part 1:", count_paths("you", "out"))
print("Part 2:", dac_fft + fft_dac)
