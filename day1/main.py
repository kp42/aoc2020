with open("./input.txt") as file:
    data = file.readlines()

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
                    print(res)
                    print(current * int_line)
                    not_found = False
                    break
