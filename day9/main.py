import itertools


def read_lines(filename):
    with open(filename) as file:
        return [int(line.strip()) for line in file.readlines()]


def first_part(lines, preamble_length):
    result = 0
    preamble_start = 0
    preamble = lines[preamble_start:preamble_length]
    index = preamble_length

    while index < len(lines):
        num = lines[index]
        if all([sum(c) != num for c in itertools.combinations(preamble, 2)]):
            result = num
            break
        else:
            preamble_start += 1
            index += 1
            preamble = lines[preamble_start : preamble_start + preamble_length]

    return result


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines, 25))


if __name__ == "__main__":
    main()
