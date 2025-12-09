import math


def parse(raw):
    return [tuple([int(x) for x in line.split(",")]) for line in raw.split("\n")]


def dist(ax, ay, az, bx, by, bz):
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2)


def part1(parsed, n):
    all_boxes = parsed
    circuits = [set([box]) for box in all_boxes]

    distances = [
        (dist(*all_boxes[i], *all_boxes[j]), all_boxes[i], all_boxes[j])
        for i in range(len(all_boxes))
        for j in range(i + 1, len(all_boxes))
    ]
    distances.sort(reverse=True)

    for i in range(n):
        _, a, b = distances.pop()
        for circuit in circuits:
            if a in circuit:
                a_circuit = circuit
            if b in circuit:
                b_circuit = circuit
        if a_circuit != b_circuit:
            for box in b_circuit:
                a_circuit.add(box)
            circuits.pop(circuits.index(b_circuit))

    m = 3
    product = 1
    circuits = [len(c) for c in circuits]
    for i in range(m):
        product *= max(circuits)
        circuits.pop(circuits.index(max(circuits)))
    return product


def part2(parsed):
    all_boxes = parsed
    circuits = [set([box]) for box in all_boxes]

    distances = [
        (dist(*all_boxes[i], *all_boxes[j]), all_boxes[i], all_boxes[j])
        for i in range(len(all_boxes))
        for j in range(i + 1, len(all_boxes))
    ]
    distances.sort(reverse=True)

    while len(circuits) > 1:
        _, a, b = distances.pop()
        for circuit in circuits:
            if a in circuit:
                a_circuit = circuit
            if b in circuit:
                b_circuit = circuit
        if a_circuit != b_circuit:
            for box in b_circuit:
                a_circuit.add(box)
            circuits.pop(circuits.index(b_circuit))

    return a[0] * b[0]


if __name__ == "__main__":
    day = 8
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw), 10)}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw), 1000)}")
        print(f"Part 2: {part2(parse(raw))}")
