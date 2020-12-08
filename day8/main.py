ACC_OP = "acc"
JUMP_OP = "jmp"
NO_OP = "nop"


def read_lines(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def first_part(lines):
    current_index = 0
    acc = 0
    visited = []

    while current_index < len(lines):
        if current_index in visited:
            break

        operation, value = lines[current_index].split(" ")
        value = int(value)
        visited.append(current_index)

        if operation == ACC_OP:
            acc += value
            current_index += 1
        if operation == JUMP_OP:
            current_index += value
        if operation == NO_OP:
            current_index += 1

    return acc


def main():
    lines = read_lines("./input.txt")
    print(first_part(lines))


if __name__ == "__main__":
    main()
