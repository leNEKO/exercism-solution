pub fn find_saddle_points(rows: &[Vec<u64>]) -> Vec<(usize, usize)> {
    // matrix size
    let h = rows.len();
    let w = rows[0].len();

    // init results
    let mut saddles: Vec<(usize, usize)> = vec![];

    // earlier return if empty input
    if !(h > 0 && w > 0) {
        return saddles;
    }

    // my "no clue" transposition
    let mut columns = vec![vec![0; h]; w];
    for (y, row) in rows.iter().enumerate() {
        for (x, val) in row.iter().enumerate() {
            columns[x][y] = val.clone();
        }
    }

    // Again his nested uglyness
    for (y, row) in rows.iter().enumerate() {
        let max_in_row = row.iter().max().unwrap();
        for (x, val) in row.iter().enumerate() {
            let min_in_col = columns[x].iter().min().unwrap();
            if (val == min_in_col) && (val == max_in_row) {
                saddles.push((y, x));
            }
        }
    }
    saddles
}
