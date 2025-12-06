def parse(raw):
    return raw.split("\n")


def solve_problems(data, ops):
    total = 0
    for inputs, op in zip(data, ops):
        if op == "*":
            answer = 1
            for n in inputs:
                answer *= n
        else:
            answer = 0
            for n in inputs:
                answer += n
        total += answer
    return total


def part1(lines):
    problems = []
    for line in lines[:-1]:
        i = 0
        for n in line.split(" "):
            if n:
                if i >= len(problems):
                    problems.append([])
                problems[i].append(int(n.strip()))
                i += 1
    ops = [op for op in lines[-1].split(" ") if op]
    return solve_problems(problems, ops)


def part2(lines):
    lines = [list(line) for line in lines]
    data_lines = lines[:-1]
    op_line = lines[-1]
    problems = []
    ops = []
    line_len = max(len(line) for line in data_lines)
    for line in data_lines:
        while len(line) < line_len:
            line.append(" ")
    while len(op_line) < line_len:
        op_line.append(" ")
    while op_line:
        problem = []
        while True:
            input = ""
            for line in data_lines:
                c = line.pop()
                if c != " ":
                    input += c
            if input:
                problem.append(int(input))
            c = op_line.pop()
            if c != " ":
                ops.append(c)
                problems.append(problem)
                break
    return solve_problems(problems, ops)


if __name__ == "__main__":
    day = 6
    with open(f"inputs/{day}.example.txt") as f:
        raw = f.read().strip()
        print(f"Example part 1: {part1(parse(raw))}")
        print(f"Example part 2: {part2(parse(raw))}")
    with open(f"inputs/{day}.txt") as f:
        raw = f.read().strip()
        print(f"Part 1: {part1(parse(raw))}")
        print(f"Part 2: {part2(parse(raw))}")
