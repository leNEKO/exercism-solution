#[derive(Debug, PartialEq, Clone)]
pub enum Value {
    Mine,
    Counter(usize),
}

#[rustfmt::skip]
static OFFSET: &[(i8, i8)] = &[
    (-1, -1), (0, -1), (1, -1),
    (-1,  0), /* P */  (1,  0),
    (-1,  1), (0,  1), (1,  1),
];

pub fn neighbor_offsets(x: i8, y: i8, width: usize) -> Vec<i8> {
    OFFSET
        .iter()
        .filter_map(|(ox, oy)| {
            let (tx, ty) = (x + *ox, y + *oy);

            if (ty >= 0) && tx < width as i8{
                Some(tx + ty * width as i8)
            } else {
                None
            }
        })
        .collect()
}

fn increment_neighbors_counter(x: usize, y: usize, width: &usize, result: &mut [Value]) {
    for offset in neighbor_offsets(x as i8, y as i8, *width) {
        if let Some(v) = result.get_mut(offset as usize) {
            *v = match v {
                Value::Counter(i) => Value::Counter(*i + 1),
                Value::Mine => Value::Mine,
            }
        }
    }
}

fn count_neighbors_mines(x: usize, y: usize, width: &usize, result: Vec<Value>) -> usize {
    let mut count = 0;
    for index in neighbor_offsets(x as i8, y as i8, *width) {
        if let Some(v) = result.get(index as usize) {
            count += match v {
                Value::Counter(_) => 0,
                Value::Mine => 1,
            }
        }
    }

    count
}

pub fn annotate(minefield: &[&str]) -> Vec<String> {
    if minefield.is_empty() {
        return Vec::new();
    }

    let width = &minefield.get(0).map(|v| v.len()).unwrap_or(0);
    if width == &0 {
        return vec!["".to_string()];
    }

    let mut result: Vec<Value> = Vec::new();

    for (y, row) in minefield.iter().enumerate() {
        for (x, cell) in row.chars().enumerate() {
            match cell {
                '*' => {
                    result.push(Value::Mine);
                    increment_neighbors_counter(x, y, width, &mut result)
                }
                ' ' => {
                    result.push(Value::Counter(count_neighbors_mines(
                        x,
                        y,
                        width,
                        result.to_vec(),
                    )));
                }
                _ => (),
            }
        }
    }

    result
        .chunks(*width)
        .map(|row| {
            row.iter()
                .map(|i| match i {
                    Value::Counter(v) => {
                        if v > &0 {
                            format!("{v}")
                        } else {
                            " ".to_string()
                        }
                    }
                    Value::Mine => "*".to_string(),
                })
                .collect::<String>()
        })
        .collect()
}
