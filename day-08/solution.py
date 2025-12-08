import math


p1 = p2 = 0

with open(0, "r") as f:
    data = [line.strip().split(",") for line in f.readlines()]

dists = {}
for i, (x, y, z) in enumerate(data):
  for xx, yy, zz in data[i+1:]:
    if (x, y, z) == (xx, yy, zz): continue
    if (x, y, z, xx, yy, zz) in dists or (xx, yy, zz, x, y, z) in dists: continue
    dist = math.sqrt((int(x)-int(xx))**2 + (int(y)-int(yy))**2 + (int(z)-int(zz))**2)
    dists[(x, y, z, xx, yy, zz)] = dist

dists = dict(sorted(dists.items(), key=lambda item: item[1]))

circuits = []
for (x, y, z, xx, yy, zz), dist in list(dists.items())[:1000]:
    first_circuit = None
    second_circuit = None
    for circuit in circuits:
        if (x, y, z) in circuit:
            first_circuit = circuit
        if (xx, yy, zz) in circuit:
            second_circuit = circuit
    if first_circuit and not second_circuit:
        first_circuit.add((xx, yy, zz))
    elif not first_circuit and second_circuit:
        second_circuit.add((x, y, z))
    elif not first_circuit and not second_circuit:
        circuits.append(set([(x, y, z), (xx, yy, zz)]))
    elif first_circuit != second_circuit:
        first_circuit.update(second_circuit)
        circuits.remove(second_circuit)

circuits = []
for i, ((x, y, z, xx, yy, zz), dist) in enumerate(list(dists.items())):
    first_circuit = None
    second_circuit = None
    for circuit in circuits:
        if (x, y, z) in circuit:
            first_circuit = circuit
        if (xx, yy, zz) in circuit:
            second_circuit = circuit
    if first_circuit and not second_circuit:
        first_circuit.add((xx, yy, zz))
    elif not first_circuit and second_circuit:
        second_circuit.add((x, y, z))
    elif not first_circuit and not second_circuit:
        circuits.append(set([(x, y, z), (xx, yy, zz)]))
    elif first_circuit != second_circuit:
        first_circuit.update(second_circuit)
        circuits.remove(second_circuit)

    if len(circuits) == 1 and len(circuits[0]) == len(data):
        print(x, xx, i)
        p2 = int(x) * int(xx)
        break

circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
print("Part 1:", math.prod([len(c) for c in circuits[:3]]))
print("Part 2:", p2)

# 1440 too low
