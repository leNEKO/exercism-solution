use std::{collections::HashMap, thread};

// lines amount approach
pub fn is_small_line_amounts(lines: &[&'static str]) -> bool {
    lines.len() < 256
}

// str size approach
pub fn is_small_str_size(lines: &[&'static str]) -> bool {
    let mut size: usize = 0;
    for line in lines.iter() {
        size += line.len();

        if size > 1024 {
            return false; // stop iterate as soon limit reach
        }
    }

    true
}

pub fn frequency(lines: &[&'static str], worker_count: usize) -> HashMap<char, usize> {
    if lines.is_empty() {
        return HashMap::new();
    }

    // parallel processing is useless overhead on small amount of data
    // totally arbitrary value
    if is_small_str_size(&lines) {
        return counter(Vec::from(lines));
    }

    let lines_per_worker = div_ceil(lines.len(), worker_count);
    let mut threads = Vec::with_capacity(worker_count);

    lines.chunks(lines_per_worker).for_each(|chunk| {
        let chunk_as_vec = Vec::from(chunk);
        let handler = thread::spawn(move || counter(chunk_as_vec));
        threads.push(handler);
    });

    let mut joined_counter = HashMap::new();

    threads
        .into_iter()
        .map(|handler| handler.join().unwrap())
        .for_each(|result| {
            for (&key, value) in result.iter() {
                let counter = joined_counter.entry(key).or_insert(0);
                *counter += value;
            }
        });

    joined_counter
}

fn counter(lines: Vec<&str>) -> HashMap<char, usize> {
    let mut worker_counter = HashMap::new();

    lines
        .iter()
        .flat_map(|line| line.chars())
        .filter(|ch| ch.is_alphabetic())
        .for_each(|ch| {
            worker_counter
                .entry(ch.to_ascii_lowercase())
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        });

    worker_counter
}
#[test]
fn counter_test() {
    let sample = vec!["aaa!a", "bb  b", "cc"];
    let expected = HashMap::from([('a', 4), ('b', 3), ('c', 2)]);

    assert_eq!(expected, counter(sample))
}

fn div_ceil(dividend: usize, divisor: usize) -> usize {
    (dividend + divisor - 1) / divisor
}
#[test]
fn div_ceil_test() {
    assert_eq!(3, div_ceil(5, 2));
    assert_eq!(3, div_ceil(7, 3));
    assert_eq!(4, div_ceil(8, 2));
}
