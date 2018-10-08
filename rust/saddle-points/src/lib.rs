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

    // storage for already found column mins
    let mut cols_min: Vec<Option<u64>> = vec![None; w];

    // let's iterate
    for (y, row) in rows.iter().enumerate() {
        let max_in_row = row.iter().max().unwrap();
        for (x, val) in row.iter().enumerate() {
            // a closure that return the min value in current column index x
            let get_min = || rows.iter().map(|row| row[x]).min().unwrap();
            // search for the min only if not found yet
            let min_in_col = cols_min[x].get_or_insert_with(get_min);

            if (min_in_col == val) && (max_in_row == val) {
                saddles.push((y, x));
            }
        }
    }

    saddles
}
