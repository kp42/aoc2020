import re
import unittest

VALID_FIELDS = [
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    "cid",  # (Country ID)
]
OPTIONAL_FIELDS = ["cid"]
REQUIRED_FIELDS = [x for x in VALID_FIELDS if x not in OPTIONAL_FIELDS]
VALID_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_hex_color(string):
    return re.search("^#(?:[0-9a-fA-F]{3}){1,2}$", string) is not None


def is_valid_color(string):
    return string in VALID_COLORS


def is_valid_passport_id(string):
    return re.search(r"^[0-9]{9}$", string) is not None


def is_valid_height(string):
    if "cm" in string:
        height = int(re.match(r"[0-9]+", string).group())
        return 150 <= height <= 193

    if "in" in string:
        height = int(re.match(r"[0-9]+", string).group())
        return 59 <= height <= 76

    return False


def is_valid_birthyear(year):
    year = int(year)
    return 1920 <= year <= 2002


def is_valid_issue_year(year):
    year = int(year)
    return 2010 <= year <= 2020


def is_valid_expire_year(year):
    year = int(year)
    return 2020 <= year <= 2030


FIELD_VALIDATORS = {
    "byr": is_valid_birthyear,
    "iyr": is_valid_issue_year,
    "eyr": is_valid_expire_year,
    "hgt": is_valid_height,
    "hcl": is_valid_hex_color,
    "ecl": is_valid_color,
    "pid": is_valid_passport_id,
    "cid": None,
}


def get_passport_fields(passport):
    return re.findall(r"\w+(?=:)", passport)


def extract_fields_and_values(passport):
    matches = re.findall(r"\w+:[\w#]+(?=)", passport)

    return [m.split(":") for m in matches]


def is_valid(fields):
    return all(x in fields for x in REQUIRED_FIELDS)


def extract_passports(data):
    passports = []
    current_passport = ""

    for index, line in enumerate(data):
        if line == "\n":
            passports.append(current_passport)
            current_passport = ""
        else:
            current_passport += line

        if index + 1 == len(data):
            passports.append(current_passport)

    return passports


def first_part(data):
    result = 0
    passports = extract_passports(data)

    for passport in passports:
        fields = get_passport_fields(passport)

        if is_valid(fields):
            result += 1

    return result


def is_valid_pair(pair):
    field_name = pair[0]
    value = pair[1]

    if callable(FIELD_VALIDATORS[field_name]):
        return FIELD_VALIDATORS[field_name](value)
    return True


def second_part(data):
    result = 0
    passports = extract_passports(data)

    for passport in passports:
        if is_valid(passport):
            pairs = extract_fields_and_values(passport)

            if all(is_valid_pair(pair) for pair in pairs):
                result += 1

    return result


class TestFirstPart(unittest.TestCase):
    def test_first_part(self):
        data = read_file("./example.txt")

        self.assertEqual(first_part(data), 2)


class TestSecondPart(unittest.TestCase):
    def test_valid(self):
        data = read_file("./valid.txt")

        self.assertEqual(second_part(data), 4)

    def test_invalid(self):
        data = read_file("./invalid.txt")

        self.assertEqual(second_part(data), 0)


def read_file(file_path):
    with open(file_path) as file:
        data = file.readlines()
        return data


if __name__ == "__main__":
    DATA = read_file("./input.txt")
    print(first_part(DATA))
    print(second_part(DATA))
