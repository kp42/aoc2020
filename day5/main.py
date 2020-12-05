import unittest

MAX_ROWS = 128
MAX_COLUMNS = 8


def calculate_seat_id(row, column):
    return (row * 8) + column


def first_half(lst):
    half = len(lst) // 2
    return lst[:half]


def second_half(lst):
    half = len(lst) // 2
    return lst[half:]


def get_row_column_pair(line):
    rows = [i for i in range(0, MAX_ROWS)]
    columns = [i for i in range(0, MAX_COLUMNS)]

    for c in line:
        if c == "F":
            rows = first_half(rows)
        if c == "B":
            rows = second_half(rows)
        if c == "L":
            columns = first_half(columns)
        if c == "R":
            columns = second_half(columns)

    return rows[0], columns[0]


def read_lines(filename):
    with open("./input.txt") as file:
        return [line.strip() for line in file.readlines()]


def first_part(lines):
    seat_id = 0

    for line in lines:
        row, column = get_row_column_pair(line)
        line_seat_id = calculate_seat_id(row, column)

        if line_seat_id > seat_id:
            seat_id = line_seat_id

    return seat_id


class TestFirstPart(unittest.TestCase):
    def test_row_column_pairs(self):
        cases = {
            "FBFBBFFRLR": (44, 5),
            "BFFFBBFRRR": (70, 7),
            "FFFBBBFRRR": (14, 7),
            "BBFFBBFRLL": (102, 4),
        }

        for (value, expected) in cases.items():
            self.assertEqual(get_row_column_pair(value), expected)

    def test_calculate_seat_id(self):
        cases = {
            "FBFBBFFRLR": 357,
            "BFFFBBFRRR": 567,
            "FFFBBBFRRR": 119,
            "BBFFBBFRLL": 820,
        }

        for (value, expected) in cases.items():
            row, column = get_row_column_pair(value)
            self.assertEqual(calculate_seat_id(row, column), expected)


if __name__ == "__main__":
    lines = read_lines("./input.txt")
    print(first_part(lines))
