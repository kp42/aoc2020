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


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))


if __name__ == "__main__":
    main()
