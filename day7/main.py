import functools
import re

SHINY_GOLD_BAG = "shiny gold"


def read_lines(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def can_contain_shiny_gold_bag(bag_type, bag_rules):
    if bag_type in bag_rules:
        return any(
            [
                i
                for i in bag_rules[bag_type]
                if can_contain_shiny_gold_bag(i, bag_rules) or i == SHINY_GOLD_BAG
            ]
        )

    return False


def extract_bag_color_rules(line):
    [bag_type, rules] = line.split(" bags contain ")
    rule_matches = re.findall(r"(?<=\d )[\w\s]+(?= bag)", rules)
    if rule_matches:
        return [bag_type, rule_matches]
    return [bag_type, []]


def first_part(lines):
    bag_rules = {}
    for line in lines:
        [bag_type, rules] = extract_bag_color_rules(line)
        bag_rules[bag_type] = rules

    result = 0

    for (bag_type, rules) in bag_rules.items():
        if can_contain_shiny_gold_bag(bag_type, bag_rules):
            result += 1

    return result


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))


if __name__ == "__main__":
    main()

