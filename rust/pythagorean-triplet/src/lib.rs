pub fn find() -> Option<i32> {
    return _find(1000);
}

pub fn _find(limit: i32) -> Option<i32> {
    for a in 3..limit / 3 {
        for b in a..limit / 2 {
            let c = limit - (a + b);
            if a * a + b * b == c * c {
                println!("({},{},{})", a, b, c);
                return Some(a * b * c);
            }
        }
    }
    None
}
