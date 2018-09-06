pub fn find() -> Option<u32> {
    match _find(1000) {
        Some(x) => return Some(x.0),
        None => None,
    }
}

pub fn _find(limit: u32) -> Option<(u32, u32)> {
    let mut i = 0u32; // uselessness counter
    for a in 3..(limit / 3) {
        for b in a..((limit - a + 1) / 2) {
            let c = limit - (a + b);
            if c < b || c > a + b {
                println!("({},{},{})", a, b, c);
                // my test need i to be 0 :)
                i += 1;
            }
            if a * a + b * b == c * c {
                return Some((a * b * c, i));
            }
        }
    }
    None
}
