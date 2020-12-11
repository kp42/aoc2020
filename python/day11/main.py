import math
from copy import deepcopy

EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."


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


def get_adjacent_seats(row_id, columnd_id, matrix):
    result = []

    if row_id > len(matrix) or columnd_id > len(matrix[row_id]):
        return result

    min_row_id = clamp(row_id - 1, 0, row_id)
    max_row_id = clamp(row_id + 2, row_id, len(matrix))
    for r in range(min_row_id, max_row_id):
        min_column_id = clamp(columnd_id - 1, 0, len(matrix[r]))
        max_column_id = clamp(columnd_id + 2, columnd_id, len(matrix[r]))
        for c in range(min_column_id, max_column_id):
            if c == columnd_id and r == row_id:
                continue
            result.append(matrix[r][c])

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

    while True:
        changes = 0
        result = 0
        for row_id, row in enumerate(matrix):
            for column_id, column in enumerate(row):
                if column == FLOOR:
                    continue

                adjacent_seats = get_adjacent_seats(row_id, column_id, matrix)

                if column == EMPTY_SEAT and not any(
                    [seat for seat in adjacent_seats if seat == OCCUPIED_SEAT]
                ):
                    next_matrix[row_id][column_id] = OCCUPIED_SEAT
                    changes += 1
                elif (
                    column in [OCCUPIED_SEAT]
                    and adjacent_occupied_seats_count(adjacent_seats) >= 4
                ):
                    next_matrix[row_id][column_id] = EMPTY_SEAT
                    changes += 1

                if next_matrix[row_id][column_id] == OCCUPIED_SEAT:
                    result += 1

        matrix = deepcopy(next_matrix)

        if changes == 0:
            break

    return result


def is_diagonal(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x1 - x2) == abs(y1 - y2)


def closeness_index(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(abs(x1 - x2) + abs(y1 - y2))


def get_visible_seats(row_id, column_id, matrix):
    # TODO: this can be improved
    result = []
    points = {
        "l-horizontal": None,
        "r-horizontal": None,
        "t-vertical": None,
        "b-vertical": None,
        "tl-diag": None,
        "tr-diag": None,
        "bl-diag": None,
        "br-diag": None,
    }

    for ri, r in enumerate(matrix):
        for ci, c in enumerate(r):
            if ri == row_id and ci == column_id:
                continue

            if c in [OCCUPIED_SEAT, EMPTY_SEAT]:
                if is_diagonal((ri, ci), (row_id, column_id)):
                    if ri < row_id and ci < column_id:
                        if points["tl-diag"] is None:
                            points["tl-diag"] = (ri, ci)
                        elif closeness_index(
                            points["tl-diag"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["tl-diag"] = (ri, ci)

                    if ri < row_id and ci > column_id:
                        if points["tr-diag"] is None:
                            points["tr-diag"] = (ri, ci)
                        elif closeness_index(
                            points["tr-diag"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["tr-diag"] = (ri, ci)

                    if ri > row_id and ci > column_id:
                        if points["br-diag"] is None:
                            points["br-diag"] = (ri, ci)
                        elif closeness_index(
                            points["br-diag"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["br-diag"] = (ri, ci)

                    if ri > row_id and ci < column_id:
                        if points["bl-diag"] is None:
                            points["bl-diag"] = (ri, ci)
                        elif closeness_index(
                            points["bl-diag"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["bl-diag"] = (ri, ci)

                if ci == column_id:
                    if ri < row_id:
                        if points["t-vertical"] is None:
                            points["t-vertical"] = (ri, ci)
                        elif closeness_index(
                            points["t-vertical"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["t-vertical"] = (ri, ci)
                    else:
                        if points["b-vertical"] is None:
                            points["b-vertical"] = (ri, ci)
                        elif closeness_index(
                            points["b-vertical"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["b-vertical"] = (ri, ci)

                if ri == row_id:
                    if ci < column_id:
                        if points["l-horizontal"] is None:
                            points["l-horizontal"] = (ri, ci)
                        elif closeness_index(
                            points["l-horizontal"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["l-horizontal"] = (ri, ci)
                    else:
                        if points["r-horizontal"] is None:
                            points["r-horizontal"] = (ri, ci)
                        elif closeness_index(
                            points["r-horizontal"], (row_id, column_id)
                        ) > closeness_index((ri, ci), (row_id, column_id)):
                            points["r-horizontal"] = (ri, ci)

    for k, v in points.items():
        if v is not None:
            ri, ci = v
            result.append((ri, ci))

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

    def leave(self, matrix):
        if matrix[self.x][self.y] == OCCUPIED_SEAT:
            takens_seats_count = 0

            for x, y in self.closest_seats:
                if matrix[x][y] == OCCUPIED_SEAT:
                    takens_seats_count += 1

            return takens_seats_count >= 5

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

        for seat in seats:
            if seat.take(matrix):
                next_matrix[seat.x][seat.y] = OCCUPIED_SEAT
                changes += 1
            elif seat.leave(matrix):
                next_matrix[seat.x][seat.y] = EMPTY_SEAT
                changes += 1

        matrix = deepcopy(next_matrix)

        if changes == 0:
            break

    for seat in seats:
        if seat.is_taken(matrix):
            result += 1

    return result


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))
    print(second_part(lines))


if __name__ == "__main__":
    main()
