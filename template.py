def parse(raw):
    pass


def part1(parsed):
    pass


def part2(parsed):
    pass


if __name__ == "__main__":
    day = {{day}}
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw))}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
