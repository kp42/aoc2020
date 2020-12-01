use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("./data/input.txt") {
        let input: Vec<i32> = lines
            .filter_map(Result::ok)
            .map(|l| l.parse::<i32>())
            .filter_map(Result::ok)
            .collect();

        println!("First part: {}", first_part(&input));
        println!("Second part: {}", second_part(&input));
    }
}

fn first_part(lines: &Vec<i32>) -> i32 {
    for i in lines {
        for j in lines {
            if j != i && i + j == 2020 {
                return j * i;
            }
        }
    }

    0
}

fn second_part(lines: &Vec<i32>) -> i32 {
    for i in lines {
        for j in lines {
            for k in lines {
                if j != i && k != i && i + j + k == 2020 {
                    return j * i * k;
                }
            }
        }
    }

    0
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
