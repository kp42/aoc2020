import itertools


def read_lines(filename):
    with open(filename) as file:
        lines = [0]
        lines.extend([int(line.strip()) for line in file.readlines()])
        lines.sort()
        return lines


def first_part(lines):
    buckets = {1: 0, 2: 0, 3: 1}

    for index, line in enumerate(lines):
        if index + 1 < len(lines):
            buckets[lines[index + 1] - line] += 1

    return buckets[1] * buckets[3]


def second_part(numbers):
    """
    CHEATING!!
    Got solution from: https://gist.github.com/Battleman/b5a6e171cc4660e69fd51507f73c9190
    """
    linkers = {n: 1 for n in numbers}
    for i, n1 in enumerate(numbers):
        for j in (i + 2, i + 3):
            if j < len(numbers) and numbers[j] - n1 <= 3:
                for n2 in numbers[j:]:
                    linkers[n2] += linkers[n1]

    return linkers[max(numbers)]


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))
    print(second_part(lines))


if __name__ == "__main__":
    main()
