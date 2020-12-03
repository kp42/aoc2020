import functools
import math
import unittest


def traverse(data, right, down=1):
    result = 0
    x = 0
    max_index = len(data) * right

    if down != 1:
        data = data[::down]

    for index, line in enumerate(data):
        if index == 0:
            continue

        x += right
        trimmed_line = line.strip()
        new_line = trimmed_line

        for _ in range(math.ceil(max_index / len(trimmed_line))):
            new_line += trimmed_line

        if new_line[x] == "#":
            result += 1

    return result


def first_part(data):
    return traverse(data, 3)


def second_part(data):
    results = [
        traverse(data, 1),
        traverse(data, 3),
        traverse(data, 5),
        traverse(data, 7),
        traverse(data, 1, 2),
    ]
    return functools.reduce(lambda x, y: x * y, results)


def read_file(file_path):
    with open(file_path) as file:
        data = file.readlines()
        return data


class TestTraverse(unittest.TestCase):
    def test_traverse(self):
        data = read_file("./example.txt")

        self.assertEqual(traverse(data, 1), 2)
        self.assertEqual(traverse(data, 3), 7)
        self.assertEqual(traverse(data, 5), 3)
        self.assertEqual(traverse(data, 7), 4)
        self.assertEqual(traverse(data, 1, 2), 2)


with open("./input.txt") as file:
    data = file.readlines()

    print(first_part(data))
    print(second_part(data))

