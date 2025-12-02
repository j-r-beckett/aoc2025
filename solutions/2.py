import re


def parse(raw):
    return [tuple(int(x) for x in r.split("-")) for r in raw.split(",")]


def sum_invalid(ranges, is_invalid):
    return sum(
        n for start, end in ranges for n in range(start, end + 1) if is_invalid(n)
    )


def part1(ranges):
    def is_invalid(id):
        return bool(re.search(r"^(.+)\1$", str(id)))

    return sum_invalid(ranges, is_invalid)


def part2(ranges):
    def is_invalid(id):
        return bool(re.search(r"^(.+)\1+$", str(id)))

    return sum_invalid(ranges, is_invalid)


if __name__ == "__main__":
    day = 2
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
