def parse(raw):
    return [list(line.strip()) for line in raw.split("\n")]


def part1(diagram):
    diagram[0][diagram[0].index("S")] = "|"
    splits = 0
    for row in range(len(diagram) - 1):
        for col in range(len(diagram[0])):
            if diagram[row][col] == "|":
                if diagram[row + 1][col] == "^":
                    splits += 1
                    if col > 0 and diagram[row + 1][col - 1] != "^":
                        diagram[row + 1][col - 1] = "|"
                    if col < len(diagram[0]) - 1 and diagram[row + 1][col + 1] != "^":
                        diagram[row + 1][col + 1] = "|"
                else:
                    diagram[row + 1][col] = "|"
    return splits


def part2(diagram):
    cache = {}

    def timelines(row, col):
        if row == len(diagram) - 1:
            return 1
        if (row, col) not in cache:
            if diagram[row + 1][col] == "^":
                result = 0
                if col > 0 and diagram[row + 1][col - 1] != "^":
                    result += timelines(row + 1, col - 1)
                if col < len(diagram[0]) - 1 and diagram[row + 1][col + 1] != "^":
                    result += timelines(row + 1, col + 1)
                cache[(row, col)] = result
            else:
                cache[(row, col)] = timelines(row + 1, col)
        return cache[(row, col)]

    return timelines(0, diagram[0].index("S"))


if __name__ == "__main__":
    day = 7
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw))}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
