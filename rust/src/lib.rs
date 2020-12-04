use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn get_lines<P>(filename: P) -> Vec<String>
where
    P: AsRef<Path>,
{
    match read_lines(filename) {
        Ok(lines) => lines.filter_map(Result::ok).collect(),
        Err(_) => Vec::new(),
    }
}
