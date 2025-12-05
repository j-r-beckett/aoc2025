def parse(raw):
    fresh, available = tuple(raw.split("\n\n"))
    fresh = [tuple(range.split("-")) for range in fresh.split("\n")]
    return [(int(a), int(b)) for a, b in fresh], [int(a) for a in available.split("\n")]


def part1(parsed):
    fresh, available = parsed
    count = 0
    for ing in available:
        for start, end in fresh:
            if ing >= start and ing <= end:
                count += 1
                break
    return count


def part2(parsed):
    fresh = parsed[0]

    length = len(fresh)
    starts = [r[0] for r in fresh]
    ends = [r[1] for r in fresh]

    starts.sort()
    ends.sort()

    total = 0
    depth = 0
    interval_start = None
    i = j = 0
    while True:
        if i < length and (j >= length or starts[i] <= ends[j]):
            if depth == 0:
                interval_start = starts[i]
            depth += 1
            i += 1
        elif j < length and (i >= length or ends[j] <= starts[i]):
            depth -= 1
            if depth == 0:
                total += ends[j] - interval_start + 1
            j += 1
        else:
            break
    return total


if __name__ == "__main__":
    day = 5
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw))}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
