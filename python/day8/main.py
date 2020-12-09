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


def get_op_value_pair(line):
    op, v = line.split(" ")
    return [op, int(v)]


def second_part(lines):
    current_index = 0
    acc = 0
    visited = []
    allowed_ops = [JUMP_OP, NO_OP]

    # brute force the corrupted value
    for i in range(0, len(lines)):
        op, v = get_op_value_pair(lines[i])

        if op in allowed_ops:
            new_lines = list(lines)
            if op == NO_OP and v > 0:
                new_lines[i] = f"{JUMP_OP} {v}"
            elif op == JUMP_OP:
                new_lines[i] = f"{NO_OP} {v}"

            while current_index < len(new_lines):
                operation, value = get_op_value_pair(new_lines[current_index])

                if current_index in visited:
                    current_index = 0
                    acc = 0
                    visited = []
                    break

                visited.append(current_index)

                if operation == ACC_OP:
                    acc += value
                    current_index += 1
                if operation == JUMP_OP:
                    current_index += value
                if operation == NO_OP:
                    current_index += 1
        else:
            continue

    return acc


def main():
    lines = read_lines("./input.txt")
    print(first_part(lines))
    print(second_part(lines))


if __name__ == "__main__":
    main()
