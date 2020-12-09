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


def extract_count_color_pairs(line):
    [bag_type, rules] = line.split(" bags contain ")
    rule_matches = re.findall(r"(?<=(\d) )([\w\s]+)(?= bag)", rules)
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


def second_part_recursion(bag_type, all_bags):
    result = 0
    bags = all_bags[bag_type]

    for (count, bag) in bags:
        if len(all_bags[bag]) == 0:
            return 1

        count = int(count)
        child = second_part_recursion(bag, all_bags)

        if child == 1:
            result += count * child
        else:
            result += count + count * child

    return result


def second_part_count_bags(bag_rules):
    def count_inner_bags(currentbag):
        return sum(
            int(count) + int(count) * count_inner_bags(bag)
            for count, bag in bag_rules[currentbag]
        )

    return count_inner_bags(SHINY_GOLD_BAG)


def second_part(lines):
    lines = read_lines("./input.txt")
    bag_rules = {}
    for line in lines:
        [color, rules] = extract_count_color_pairs(line)
        bag_rules[color] = rules

    return second_part_count_bags(bag_rules)


def main():
    lines = read_lines("./input.txt")

    print(first_part(lines))
    print(second_part(lines))


if __name__ == "__main__":
    main()

