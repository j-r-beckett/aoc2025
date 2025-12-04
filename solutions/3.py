def parse(raw):
    return raw.split("\n")


def max_total_joltage(banks, batteries):
    cache = {}

    def max_joltage(bank, n):
        assert len(bank) > 0 and n > 0
        if (bank, n) not in cache:
            if len(bank) == n:
                v = int("".join(bank))
            elif n == 1:
                v = max([int(j) for j in bank])
            else:
                v = max(
                    int(bank[0] + str(max_joltage(bank[1:], n - 1))),
                    max_joltage(bank[1:], n),
                )
            cache[(bank, n)] = v
        return cache[(bank, n)]

    return sum(max_joltage(bank, batteries) for bank in banks)


def part1(parsed):
    return max_total_joltage(parsed, 2)


def part2(parsed):
    return max_total_joltage(parsed, 12)


if __name__ == "__main__":
    day = 3
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
