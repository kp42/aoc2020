use aoc::read_lines;

fn main() {
    if let Ok(lines) = read_lines("./data/day2.txt") {
        let result = lines
            .filter_map(Result::ok)
            .filter(|l| first_part_is_valid(l.to_string()))
            .collect::<Vec<String>>()
            .len();
        println!("First part: {:#?}", result);
    }
    if let Ok(lines) = read_lines("./data/day2.txt") {
        let result = &lines
            .filter_map(Result::ok)
            .filter(|l| second_part_is_valid(l.to_string()))
            .collect::<Vec<String>>()
            .len();
        println!("Second part: {:#?}", result);
    }
}

fn first_part_is_valid(line: String) -> bool {
    let data: Vec<&str> = line.split(":").collect();
    let policy: Vec<&str> = data[0].split(" ").collect();
    let password = data[1];
    let letter = policy[1];
    let min_count = policy[0].split("-").collect::<Vec<&str>>()[0];
    let max_count = policy[0].split("-").collect::<Vec<&str>>()[1];
    let letter_count = password.matches(letter).count();

    letter_count >= min_count.parse::<usize>().unwrap()
        && letter_count <= max_count.parse::<usize>().unwrap()
}

fn second_part_is_valid(line: String) -> bool {
    let data: Vec<&str> = line.split(":").collect();
    let policy: Vec<&str> = data[0].split(" ").collect();
    let password = data[1].trim();
    let letter = policy[1];
    let first_position = policy[0].split("-").collect::<Vec<&str>>()[0]
        .parse::<usize>()
        .unwrap()
        - 1;
    let second_position = policy[0].split("-").collect::<Vec<&str>>()[1]
        .parse::<usize>()
        .unwrap()
        - 1;
    let first_position_char = get_at(password, first_position);
    let second_position_char = get_at(password, second_position);

    if let (Some(first_char), Some(second_char)) = (first_position_char, second_position_char) {
        return first_char == letter && second_char != letter
            || first_char != letter && second_char == letter;
    }
    false
}

fn get_at(value: &str, index: usize) -> Option<String> {
    match value.clone().chars().nth(index) {
        Some(c) => Some(c.to_string()),
        None => None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_first_part_is_valid() {
        assert_eq!(first_part_is_valid("1-3 a: abcde".to_string()), true);
        assert_eq!(first_part_is_valid("1-3 b: cdefg".to_string()), false);
        assert_eq!(first_part_is_valid("2-9 c: ccccccccc".to_string()), true);
    }

    #[test]
    fn test_second_part_is_valid() {
        assert_eq!(second_part_is_valid("1-3 a: abcde".to_string()), true);
        assert_eq!(second_part_is_valid("1-3 b: cdefg".to_string()), false);
        assert_eq!(second_part_is_valid("2-9 c: ccccccccc".to_string()), false);
    }
}
