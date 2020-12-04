use aoc::get_lines;

fn main() {
    let data = get_lines("./data/day3.txt");
    println!("{}", first_part(&data));
    println!("{}", second_part(&data));
}

fn first_part(data: &Vec<String>) -> usize {
    traverse(data, 1, None)
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
    let lines_count = data.len();
    let mut result = 0;
    let mut x = 0;
    let max_index = lines_count * right;

    for (index, line) in lines.enumerate() {
        if index == 0 {
            continue;
        }

        x += right;
        let trimmed_line = line.trim();
        let mut new_line = trimmed_line.to_string();
        let range = divide_ceil(max_index, trimmed_line.len());

        for _ in 0..range {
            new_line.push_str(trimmed_line);
        }

        match new_line.chars().nth(x) {
            Some(c) => {
                if c == '#' {
                    result += 1
                }
            }
            _ => (),
        }
    }

    result
}

fn divide_ceil(a: usize, b: usize) -> usize {
    ((a / b) as f64).ceil() as usize
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
