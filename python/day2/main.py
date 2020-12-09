def first_part(data):
    result = 0

    for line in data:
        line_data = line.strip().split(":")
        policy = line_data[0].split(" ")
        password = line_data[1]
        letter = policy[1]
        min_count = int(policy[0].split("-")[0])
        max_count = int(policy[0].split("-")[1])
        letter_count = password.count(letter)
        if letter_count >= min_count and letter_count <= max_count:
            result += 1

    return result


def second_part(data):
    result = 0

    for line in data:
        line_data = line.strip().split(":")
        policy = line_data[0].split(" ")
        password = line_data[1].strip()
        letter = policy[1]
        first_position = int(policy[0].split("-")[0]) - 1
        second_position = int(policy[0].split("-")[1]) - 1

        if (
            password[first_position] == letter
            and password[second_position] != letter
            or password[first_position] != letter
            and password[second_position] == letter
        ):
            result += 1

    return result


with open("./input.txt") as file:
    data = file.readlines()

    print(first_part(data))
    print(second_part(data))

