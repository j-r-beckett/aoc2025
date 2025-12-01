def part1(data):
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    day = {{day}}
    with open(f"inputs/{day}.txt") as f:
        data = f.read().strip()
        print(f"Part 1: {part1(data)}")
        print(f"Part 2: {part2(data)}")
