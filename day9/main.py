import itertools


def read_lines(filename):
    with open(filename) as file:
        return [int(line.strip()) for line in file.readlines()]


def get_invalid_number(lines, preamble_length):
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


def get_contigious_set(lines, invalid_number):
    # https://stackoverflow.com/a/46941568
    result = []
    for s, e in itertools.combinations(range(len(lines) + 1), 2):
        if len(lines[s:e]) >= 2:
            result.append(lines[s:e])

    return result


def first_part(lines, preamble_length):
    return get_invalid_number(lines, preamble_length)


def second_part(lines, preamble_length):
    invalid_number = get_invalid_number(lines, preamble_length)
    sets = get_contigious_set(lines, invalid_number)
    result = 0

    for s in sets:
        if sum(s) == invalid_number:
            result = min(s) + max(s)

    return result


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines, 25))
    print(second_part(lines, 25))


if __name__ == "__main__":
    main()
