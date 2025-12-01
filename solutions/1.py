import re


def parse(data):
    return [(line[0], int(line[1:])) for line in data.split()]


def part1(data):
    data = parse(data)
    curr = 50
    count = 0
    for direction, n in data:
        if direction == 'L':
            n *= -1
        curr = (curr + n) % 100    
        if curr == 0:
            count += 1
    return count


def part2(data):
    data = parse(data)
    curr = 50
    count = 0
    for direction, n in data:
        while n != 0:
            if direction == 'L':
                curr -= 1
            else:
                curr += 1
            n -= 1
            curr = curr % 100
            if curr == 0:
                count += 1
    return count
            


if __name__ == "__main__":
    day = 1
    with open(f"inputs/{day}.txt") as f:
        data = f.read().strip()
        print(f"Part 1: {part1(data)}")
        print(f"Part 2: {part2(data)}")
