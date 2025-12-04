def parse(raw):
    return [list(line) for line in raw.split("\n")]


def adjacent(map, row, col):
    result = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                r = row + i
                c = col + j
                if r >= 0 and r < len(map) and c >= 0 and c < len(map[0]):
                    result.append(map[r][c])
    return result


def part1(map):
    return sum(
        map[row][col] == "@"
        and len([a for a in adjacent(map, row, col) if a == "@"]) < 4
        for row in range(len(map))
        for col in range(len(map[0]))
    )


def part2(map):
    total_num_removed = 0
    num_removed = -1
    while num_removed != 0:
        num_removed = 0
        for row in range(len(map)):
            for col in range(len(map[0])):
                if (
                    map[row][col] == "@"
                    and len([a for a in adjacent(map, row, col) if a == "@"]) < 4
                ):
                    map[row][col] = "."
                    num_removed += 1
        total_num_removed += num_removed
    return total_num_removed


if __name__ == "__main__":
    day = 4
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw))}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
