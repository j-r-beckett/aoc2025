import re


def parse(raw):
    return [tuple(int(x) for x in r.split("-")) for r in raw.split(",")]


def is_invalid_p1(id):
    return bool(re.search(r"^(.+)\1$", id))


def is_invalid_p2(id):
    return bool(re.search(r"^(.+)\1+$", id))


def part1(parsed):
    count = 0
    for start, end in parsed:
        for i in range(start, end + 1):
            if is_invalid_p1(str(i)):
                count += i
    return count


def part2(parsed):
    count = 0
    for start, end in parsed:
        for i in range(start, end + 1):
            if is_invalid_p2(str(i)):
                count += i
    return count


if __name__ == "__main__":
    day = 2
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw))}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
