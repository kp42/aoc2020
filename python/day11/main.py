import math
from copy import deepcopy

EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."
DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
]


def read_lines(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def to_matrix(lines):
    matrix = []

    for line in lines:
        matrix.append([c for c in line])

    return matrix


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def get_adjacent_seats(row_id, col_id, matrix):
    result = []
    for row_inc, col_inc in DIRECTIONS:
        rid = row_id + row_inc
        cid = col_id + col_inc

        if rid >= 0 and rid < len(matrix) and cid >= 0 and cid < len(matrix[rid]):
            seat = matrix[rid][cid]

            if seat in [OCCUPIED_SEAT, EMPTY_SEAT]:
                result.append((rid, cid))

    return result


def print_matrix(matrix):
    result = ""
    for row in matrix:
        row_str = ""
        for col in row:
            row_str += col
        row_str += "\n"
        result += row_str
    return result


def adjacent_occupied_seats_count(seats):
    result = 0

    for s in seats:
        if s == OCCUPIED_SEAT:
            result += 1

    return result


def first_part(lines):
    matrix = to_matrix(lines)
    next_matrix = deepcopy(matrix)
    changes = 0
    result = 0
    seats = []

    for row_id, row in enumerate(matrix):
        for column_id, column in enumerate(row):
            if column == FLOOR:
                continue

            seat = Seat(
                row_id, column_id, get_adjacent_seats(row_id, column_id, matrix)
            )
            seats.append(seat)

    while True:
        changes = 0
        result = 0

        for seat in seats:
            if seat.take(matrix):
                next_matrix[seat.x][seat.y] = OCCUPIED_SEAT
                changes += 1
            elif seat.leave(matrix, 4):
                next_matrix[seat.x][seat.y] = EMPTY_SEAT
                changes += 1

            if seat.is_taken(matrix):
                result += 1

        matrix = deepcopy(next_matrix)

        if changes == 0:
            break

    return result


def get_visible_seats(row_id, col_id, matrix):
    result = []
    for row_inc, col_inc in DIRECTIONS:
        rid = row_id + row_inc
        cid = col_id + col_inc

        while rid >= 0 and rid < len(matrix) and cid >= 0 and cid < len(matrix[rid]):
            seat = matrix[rid][cid]

            if seat in [OCCUPIED_SEAT, EMPTY_SEAT]:
                result.append((rid, cid))
                break

            rid += row_inc
            cid += col_inc

    return result


class Seat:
    def __init__(self, x, y, closest_seats=[]):
        self.x = x
        self.y = y
        self.closest_seats = closest_seats

    def take(self, matrix):
        if matrix[self.x][self.y] == EMPTY_SEAT:
            can_take = not any(
                [matrix[x][y] == OCCUPIED_SEAT for x, y in self.closest_seats]
            )

            return can_take

        return False

    def leave(self, matrix, threshold):
        if matrix[self.x][self.y] == OCCUPIED_SEAT:
            takens_seats_count = 0

            for x, y in self.closest_seats:
                if matrix[x][y] == OCCUPIED_SEAT:
                    takens_seats_count += 1

            return takens_seats_count >= threshold

        return False

    def is_taken(self, matrix):
        return matrix[self.x][self.y] == OCCUPIED_SEAT


def second_part(lines):
    matrix = to_matrix(lines)
    next_matrix = deepcopy(matrix)
    changes = 0
    result = 0
    seats = []

    # Modify matrix in place
    # Create seat class for all seats with
    # - position of seat
    # - closest seats in all eight directions
    for row_id, row in enumerate(matrix):
        for column_id, column in enumerate(row):
            if column == FLOOR:
                continue

            seat = Seat(row_id, column_id, get_visible_seats(row_id, column_id, matrix))
            seats.append(seat)

    while True:
        changes = 0
        result = 0

        for seat in seats:
            if seat.take(matrix):
                next_matrix[seat.x][seat.y] = OCCUPIED_SEAT
                changes += 1
            elif seat.leave(matrix, 5):
                next_matrix[seat.x][seat.y] = EMPTY_SEAT
                changes += 1

            if seat.is_taken(matrix):
                result += 1

        matrix = deepcopy(next_matrix)

        if changes == 0:
            break

    return result


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))
    print(second_part(lines))


if __name__ == "__main__":
    main()
