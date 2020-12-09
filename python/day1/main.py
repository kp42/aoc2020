import functools
import random


def first_part(data):
    current = None
    used_lines = []
    not_found = True

    while not_found:
        current = None
        for line in data:
            int_line = int(line)
            if current is None and int_line not in used_lines:
                current = int_line
                used_lines.append(int_line)
            elif current is not None:
                res = current + int_line
                if res == 2020:
                    print("First part:", current * int_line)
                    not_found = False
                    break


def second_part(data):
    items = [0, 0, 0]

    while sum_of_items(items) != 2020:
        items = [random.choice(data), random.choice(data), random.choice(data)]
    print("Second part:", functools.reduce(lambda a, b: int(a) * int(b), items))


def sum_of_items(items):
    return functools.reduce(lambda a, b: int(a) + int(b), items)


with open("./input.txt") as file:
    data = file.readlines()

    first_part(data)
    second_part(data)

