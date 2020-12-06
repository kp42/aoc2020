import string


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def first_part(lines):
    group_of_answers = []
    current_group = []
    for index, line in enumerate(lines):
        stripped_line = line.strip()

        if stripped_line == "":
            group_of_answers.append("".join(current_group))
            current_group = []
        elif index + 1 == len(lines):
            current_group.append(stripped_line)
            group_of_answers.append("".join(current_group))
        else:
            current_group.append(stripped_line)

    result = 0

    for group in group_of_answers:
        result += len(set(group))

    return result


def second_part(lines):
    group_of_answers = []
    current_group = []
    result = 0
    for index, line in enumerate(lines):
        stripped_line = line.strip()

        if stripped_line == "":
            group_of_answers.append(current_group)
            current_group = []
        elif index + 1 == len(lines):
            current_group.append(stripped_line)
            group_of_answers.append(current_group)
        else:
            current_group.append(stripped_line)

    for group in group_of_answers:
        for letter in string.ascii_lowercase:
            if all([letter in answer for answer in group]):
                result += 1

    return result


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))
    print(second_part(lines))


if __name__ == "__main__":
    main()
