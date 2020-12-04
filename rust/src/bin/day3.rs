use aoc::get_lines;

fn main() {
    let data = get_lines("./data/day3.txt");
    println!("{}", first_part(&data));
    println!("{}", second_part(&data));
}

fn first_part(data: &Vec<String>) -> usize {
    traverse(data, 3, None)
}

fn second_part(data: &Vec<String>) -> usize {
    vec![
        traverse(&data, 1, None),
        traverse(&data, 3, None),
        traverse(&data, 5, None),
        traverse(&data, 7, None),
        traverse(&data, 1, Some(2)),
    ]
    .iter()
    .fold(1, |acc, v| acc * v)
}

fn traverse(data: &Vec<String>, right: usize, down: Option<usize>) -> usize {
    let lines = data.iter().step_by(down.unwrap_or(1));
    let mut result = 0;
    let mut x = 0;

    for (index, line) in lines.enumerate() {
        if index == 0 {
            continue;
        }

        x += right;
        let trimmed_line = line.trim();

        if has_char_at(trimmed_line.to_string(), x) {
            result += 1;
        }
    }

    result
}

fn has_char_at(value: String, mut index: usize) -> bool {
    while index >= value.len() {
        index -= value.len();
    }

    match value.chars().nth(index) {
        Some(c) => c == '#',
        _ => false,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_traverse() {
        let lines = get_lines("./data/day3_example.txt");
        assert_eq!(traverse(&lines, 1, None), 2);
        assert_eq!(traverse(&lines, 3, None), 7);
        assert_eq!(traverse(&lines, 5, None), 3);
        assert_eq!(traverse(&lines, 7, None), 4);
        assert_eq!(traverse(&lines, 1, Some(2)), 2);
    }
}
